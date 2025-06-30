from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from src.scrapers.scrapy_crawler.spiders.remoteok_spider import RemoteOKSpider

def run_scrapy_spider():
    configure_logging()

    process = CrawlerProcess(settings={
        "LOG_LEVEL": "INFO",
        "FEEDS": {
            "data_output/remoteok_scrapy_output.json": {
                "format": "json",
                "overwrite": True,
            }
        },
        "USER_AGENT": "Mozilla/5.0",
        "ROBOTSTXT_OBEY": False
    })

    process.crawl(RemoteOKSpider)
    process.start()

if __name__ == "__main__":
    run_scrapy_spider()
