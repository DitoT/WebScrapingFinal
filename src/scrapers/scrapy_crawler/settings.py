BOT_NAME = 'remoteok_crawler'

SPIDER_MODULES = ['src.scrapers.scrapy_crawler.spiders']
NEWSPIDER_MODULE = 'src.scrapers.scrapy_crawler.spiders'

ROBOTSTXT_OBEY = False
LOG_LEVEL = 'WARNING'
