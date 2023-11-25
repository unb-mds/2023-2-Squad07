import os
import json

class DiarioPipeline:
    def open_spider(self, spider):
        self.results = {}  # Inicialize um dicionário vazio para os resultados

    def process_item(self, item, spider):
        # Extraia os detalhes do item
        pdf_filename = item['pdf_filename']
        municipio = item['municipio']
        data_pdf = item['data_pdf']
        num_avisos_licitacao = item['num_avisos_licitacao']

        # Crie um dicionário para armazenar os dados
        data_dict = {
            "pdf_filename": pdf_filename,
            "municipio": municipio,
            "data_pdf": data_pdf,
            "num_avisos_licitacao": num_avisos_licitacao
        }

        # Se o município já existe no dicionário, adicione os dados ao município existente
        if municipio in self.results:
            self.results[municipio].append(data_dict)
        else:
            # Caso contrário, crie uma lista para o município e adicione os dados
            self.results[municipio] = [data_dict]

        return item

    def close_spider(self, spider):
        # Ajuste o caminho para a pasta "public" no mesmo nível que a pasta "src"
        output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '../../public')
        os.makedirs(output_dir, exist_ok=True)

        # Para cada município, carregue os resultados antigos (se existirem)
        for municipio, data_list in self.results.items():
            output_file = os.path.join(output_dir, f'{municipio.lower()}_resultados.json')

            # Tente carregar os resultados antigos se o arquivo existir
            old_data = []
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as json_file:
                    old_data = json.load(json_file)

            # Adicione os novos resultados aos resultados antigos
            all_data = old_data + data_list

            # Salve os resultados combinados em um único arquivo JSON
            with open(output_file, 'w', encoding='utf-8') as json_file:
                json.dump(all_data, json_file, indent=2, default=str, ensure_ascii=False)
