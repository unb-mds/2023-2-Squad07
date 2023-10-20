import scrapy

class DiarioItem(scrapy.Item):
    pdf_filename = scrapy.Field()
    num_avisos_licitacao = scrapy.Field()