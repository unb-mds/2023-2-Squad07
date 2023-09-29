import scrapy
from pdf_spider.items import PdfTextItem
import PyPDF2

class PdfSpider(scrapy.Spider):
    name = 'pdf_spider'
    allowed_domains = ['juazeirodonorte.ce.gov.br']
    start_urls = ['https://juazeirodonorte.ce.gov.br/arquivos_download.php?id=3653&pg=diariooficial']
    text = ''  # Variável de classe para armazenar o texto extraído

    def parse(self, response):
        # Baixe o arquivo PDF
        pdf_path = 'spider01Teste.pdf'
        with open(pdf_path, 'wb') as f:
            f.write(response.body)

        # Extraia o texto do PDF usando PdfReader
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        for page in pdf_reader.pages:
            self.text += page.extract_text() + '\n'  # Adicione '\n' para separar páginas

        # Crie um item com o texto extraído
        item = PdfTextItem()
        item['text'] = self.text
        yield item

    def closed(self, reason):
        self.logger.info("Spider fechado com a razão: %s", reason)

        # Quando o spider é fechado, este método é chamado
        # Aqui você pode fazer o que quiser com o texto extraído
        # Por exemplo, salvar o texto em um arquivo de texto
        with open('texto_extraido_teste.txt', 'w', encoding='utf-8') as file:
            file.write(self.text)
