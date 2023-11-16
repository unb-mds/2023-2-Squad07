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
        # Garanta que a pasta "public" exista
        os.makedirs('../../public', exist_ok=True)

        # Combine os resultados de todos os municípios em uma única lista
        all_results = []
        for municipio, data_list in self.results.items():
            all_results.extend(data_list)

        # Salve a lista completa de resultados no arquivo JSON geral
        output_file = os.path.join('../../public', 'resultados.json')
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(all_results, json_file, indent=2, default=str, ensure_ascii=False)

        return None
