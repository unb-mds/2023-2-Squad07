import scrapy
import PyPDF2
import re  # Importe a biblioteca de expressões regulares
from pdf_spider.items import PdfTextItem

class PdfSpider(scrapy.Spider):
    name = 'pdf_spider'
    allowed_domains = ['juazeirodonorte.ce.gov.br']
    start_urls = ['https://juazeirodonorte.ce.gov.br/arquivos_download.php?id=3652&pg=diariooficial']
    text = ''  # Variável de classe para armazenar o texto extraído
    word_to_count = "licitação"  # Defina a palavra que você deseja contar

    def parse(self, response):
        # Baixe o arquivo PDF
        pdf_path = 'spiderDiario2709.pdf'
        with open(pdf_path, 'wb') as f:
            f.write(response.body)

        # Extraia o texto do PDF usando PdfReader
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        for page in pdf_reader.pages:
            self.text += page.extract_text() + '\n'  # Adicione '\n' para separar páginas

        # Pré-processamento: remover caracteres especiais e espaços em branco extras
        self.text = re.sub(r'\W+', ' ', self.text)

        # Crie um item com o texto extraído
        item = PdfTextItem()
        item['text'] = self.text
        yield item

    def closed(self, reason):
        self.logger.info("Spider fechado com a razão: %s", reason)

        # Pré-processamento: converter texto para letras minúsculas antes de contar a palavra
        lowercase_text = self.text.lower()
        lowercase_word = self.word_to_count.lower()
        
        # Contagem da palavra
        word_count = lowercase_text.count(lowercase_word)

        # Quando o spider é fechado, este método é chamado
        # Aqui você pode fazer o que quiser com o texto extraído
        # Por exemplo, salvar o texto em um arquivo de texto e a contagem da palavra
        with open('texto_puro_extraido_2709.txt', 'w', encoding='utf-8') as file:
            file.write(self.text)
        with open('contagem_palavra_2709.txt', 'w', encoding='utf-8') as file:
            file.write(f"A palavra '{self.word_to_count}' apareceu {word_count} vezes no PDF.")
