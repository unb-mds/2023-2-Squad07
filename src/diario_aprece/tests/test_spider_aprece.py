import unittest
from scrapy.http import TextResponse
from scrapy.utils.test import get_crawler
from scrapy.spiders import Spider
from diario_aprece.spiders.spider_aprece import SpiderApreceSpider

class TestSpiderAprece(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(SpiderApreceSpider)
        self.spider = SpiderApreceSpider.from_crawler(self.crawler)

    def test_parse_method(self):
        
        pdf_content = "Abaiara Aviso de Licitação"
        response = TextResponse(url="https://www.diariomunicipal.com.br", body=pdf_content)

        results = list(self.spider.parse(response))

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['municipio'], 'SeuMunicipio')
        

if __name__ == '__main__':
    unittest.main()
