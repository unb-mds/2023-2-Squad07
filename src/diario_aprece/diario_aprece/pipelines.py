import os
import json
from unidecode import unidecode
from collections import defaultdict

class DiarioPipeline:
    def open_spider(self, spider):
        self.results = defaultdict(list)  # Use defaultdict para evitar verificações desnecessárias de existência de chave

    def process_item(self, item, spider):
        # Extraia os detalhes do item
        municipio = item['municipio']
        data_pdf = item['data_pdf']
        num_avisos_licitacao = item['num_avisos_licitacao']

        # Crie um dicionário para armazenar os dados
        data_dict = {
            "municipio": municipio,
            "data_pdf": data_pdf,
            "num_avisos_licitacao": num_avisos_licitacao
        }

        # Remova acentos e caracteres especiais do nome do município para uso no nome do arquivo JSON
        clean_municipio = unidecode(municipio.lower()).replace(' ', '-')

        # Adicione os dados ao dicionário usando o mês como chave
        month_key = data_pdf.split()[2]  # Obtém o mês do campo 'data_pdf'
        self.results[clean_municipio].append(data_dict)

        return item

    def close_spider(self, spider):
        # Ajuste o caminho para a pasta "public" no mesmo nível que a pasta "src"
        output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '../../public')
        os.makedirs(output_dir, exist_ok=True)

        # Para cada município, carregue os resultados antigos (se existirem)
        for clean_municipio, data_list in self.results.items():
            output_file = os.path.join(output_dir, f'{clean_municipio}.json')

            # Tente carregar os resultados antigos se o arquivo existir
            old_data = []
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as json_file:
                    old_data = json.load(json_file)

            # Remova o campo "pdf_filename" de todos os dicionários na lista
            data_list_no_filename = [
                {key: value for key, value in data.items() if key != 'pdf_filename'}
                for data in data_list
            ]

            # Adicione os novos resultados aos resultados antigos
            all_data = old_data + data_list_no_filename

            # Salve os resultados combinados em um único arquivo JSON
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(all_data, json_file, indent=2, default=str, ensure_ascii=False)

            # Calcular a soma dos num_avisos_licitacao para cada mês
            monthly_sums = defaultdict(int)
            for data in all_data:
                month_key = data['data_pdf'].split()[2]
                monthly_sums[month_key] += data['num_avisos_licitacao']

            # Adicionar a soma mensal ao dicionário
            monthly_sums_data = [
                {
                    'municipio': clean_municipio,
                    'month': month,
                    'sum_num_avisos_licitacao': total
                }
                for month, total in monthly_sums.items()
            ]

            # Salvar o arquivo com a soma mensal
            monthly_sums_output_file = os.path.join(output_dir, f'{clean_municipio}_monthly_sums.json')
            with open(monthly_sums_output_file, 'w', encoding='utf-8') as monthly_sums_json_file:
                json.dump(monthly_sums_data, monthly_sums_json_file, indent=2, default=str, ensure_ascii=False)
