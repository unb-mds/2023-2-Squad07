# Scrapy settings for diario_aprece project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "diario_aprece"

SPIDER_MODULES = ["diario_aprece.spiders"]
NEWSPIDER_MODULE = "diario_aprece.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "diario_aprece (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Configure item pipelines
ITEM_PIPELINES = {
    'diario_aprece.pipelines.DiarioPipeline': 300,
}

# Configure output settings
FEED_FORMAT = 'json'  # Use 'json' para um único arquivo JSON
# FEED_URI = 'resultados.json'  # Esta configuração não será usada, pois cada município agora tem seu próprio arquivo

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
