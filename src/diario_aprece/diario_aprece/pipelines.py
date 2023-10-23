import os
import json

class DiarioPipeline:
    def open_spider(self, spider):
        self.results = []  # Inicialize uma lista vazia para os resultados

    def process_item(self, item, spider):
        self.results.append(dict(item))  # Adicione os resultados à lista
        return item

    def close_spider(self, spider):
        # Determine o nome do arquivo
        output_file = os.path.join('../../public', 'resultados.json')

        # Se o arquivo já existe, leia os resultados anteriores
        try:
            with open(output_file, 'r', encoding='utf-8') as json_file:
                existing_results = json.load(json_file)
        except FileNotFoundError:
            existing_results = []

        # Adicione os novos resultados aos resultados existentes
        existing_results.extend(self.results)

        # Garanta que a pasta "public" exista
        os.makedirs('../../public', exist_ok=True)

        # Salve a lista completa de resultados no arquivo
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(existing_results, json_file, indent=2, default=str, ensure_ascii=False)

        return None
