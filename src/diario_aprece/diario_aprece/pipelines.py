import json

class DiarioPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        # Aqui você pode personalizar a saída, como salvar em um arquivo JSON.
        with open('resultados.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.items, json_file, ensure_ascii=False, indent=4)

        # Alternativamente, você pode realizar outras ações, como inserir os dados em um banco de dados.

        # Lembre-se de ajustar o nome do arquivo e o formato de saída conforme necessário.

