import scrapy
import os
from diario_aprece.items import DiarioItem

class SpiderApreceSpider(scrapy.Spider):
    name = "spider_aprece"
    allowed_domains = ["www.diariomunicipal.com.br"]
    start_urls = ["https://www-storage.voxtecnologia.com.br/?m=sigpub.publicacao&f=764&i=publicado_93033_2023-10-17_b790e353b08b74cf8ec512b71603e995.pdf"]

    def parse(self, response):
        # Aqui fazemos o download do PDF
        pdf_url = response.url
        pdf_filename = os.path.basename(pdf_url)

        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(response.body)

        # Chamamos o Apache Tika para extrair o texto do PDF
        text = self.extract_text_from_pdf(pdf_filename)

        # Aqui você pode processar o texto extraído, por exemplo, separar os municípios e contar os avisos de licitação.

        # Exemplo: Contar o número de ocorrências de "Aviso de Licitação" no texto
        num_avisos_licitacao = text.lower().count("aviso de licitação")

        # Exemplo de como armazenar em um item
        item = DiarioItem(pdf_filename=pdf_filename, num_avisos_licitacao=num_avisos_licitacao)
        yield item

        # Após a raspagem e armazenamento dos dados, removemos o arquivo PDF
        os.remove(pdf_filename)

    def extract_text_from_pdf(self, pdf_filename):
        # Aqui você chama o Apache Tika para extrair o texto do PDF e o retorna.
        # A instalação e configuração do Apache Tika são necessárias.
        # Você pode usar a biblioteca 'tika' do Python para isso.
        from tika import parser

        raw_text = ""
        parsed_pdf = parser.from_file(pdf_filename)

        if 'content' in parsed_pdf:
            raw_text = parsed_pdf['content']

        return raw_text
