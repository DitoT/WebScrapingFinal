from scrapy.crawler import CrawlerProcess
from src.scrapers.scrapy_crawler.spiders.remoteok_spider import RemoteOKSpider
from src.scrapers.scrapy_crawler import settings

def run_scrapy_spider():
    process = CrawlerProcess(settings=settings.__dict__)
    process.crawl(RemoteOKSpider)
    process.start()
