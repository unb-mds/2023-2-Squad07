import scrapy
import os
from diario_aprece.items import DiarioItem
import re
import fitz  # PyMuPDF
from diario_aprece.municipios_aprece import MUNICIPIOS_APRECE

class SpiderApreceSpider(scrapy.Spider):
    name = "spider_aprece"
    allowed_domains = ["www.diariomunicipal.com.br"]
    start_urls = [input("Insira o link: ")]

    def parse(self, response):
        pdf_url = response.url
        pdf_filename = os.path.basename(pdf_url)

        with open(pdf_filename, 'wb') as pdf_file:
            pdf_file.write(response.body)

        text = self.extract_text_from_pdf(pdf_filename)

        # Extrair a data do início do PDF
        data_pdf = self.extract_data_from_text(text)

        # Iterar sobre os municípios
        for municipio in MUNICIPIOS_APRECE:
            # Verificar se o município está no texto
            if municipio.lower() in text.lower():
                # Extrair bloco de texto correspondente ao município
                municipio_block = self.extract_municipio_block(text, municipio)

                # Adicionando lógica para contar o número de avisos de licitação
                num_avisos_licitacao = municipio_block.lower().count("aviso de licitação")

                item = DiarioItem(pdf_filename=pdf_filename, municipio=municipio, data_pdf=data_pdf, num_avisos_licitacao=num_avisos_licitacao)
                yield item

        os.remove(pdf_filename)

    def extract_text_from_pdf(self, pdf_filename):
        text = ""
        try:
            # Usando a biblioteca PyMuPDF para extrair o texto do PDF
            pdf_document = fitz.open(pdf_filename)
            num_pages = pdf_document.page_count

            for page_num in range(num_pages):
                page = pdf_document[page_num]
                text += page.get_text()

        except Exception as e:
            self.logger.error(f"Erro ao extrair texto do PDF: {e}")

        return text

    def extract_municipio_block(self, text, municipio):
        # Utilizando expressão regular para encontrar o bloco de texto correspondente ao município
        match = re.search(rf'{municipio}.*?(?={("|".join(MUNICIPIOS_APRECE))})', text, re.DOTALL | re.IGNORECASE)
        return match.group(0) if match else ""

    def extract_data_from_text(self, text):
        # Tentar extrair a data no formato "DD de [Mês] de YYYY"
        match = re.search(r'(\d{1,2} de [a-zA-Z]+ de \d{4})', text)
        if match:
            return match.group(1)

        # Tentar extrair a data no formato "DD/MM/YYYY"
        match = re.search(r'(\d{2}/\d{2}/\d{4})', text)
        if match:
            return match.group(1)

        return "Data Desconhecida"
