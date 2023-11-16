# items.py
import scrapy

class DiarioItem(scrapy.Item):
    pdf_filename = scrapy.Field()
    data_pdf = scrapy.Field()
    num_avisos_licitacao = scrapy.Field()
    municipio = scrapy.Field()
