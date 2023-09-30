# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PdfTextItem(scrapy.Item):
    text = scrapy.Field()
    word_count = scrapy.Field()

