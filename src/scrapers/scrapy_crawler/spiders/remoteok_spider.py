import scrapy
from src.scrapers.scrapy_crawler.items import JobItem
import json

class RemoteOKSpider(scrapy.Spider):
    name = "remoteok"
    start_urls = ['https://remoteok.com/api']

    def parse(self, response):
        try:
            data = json.loads(response.body)[1:]  # Skip metadata
        except Exception as e:
            self.logger.error(f"Failed to parse JSON: {e}")
            return

        for job in data[:10]:  # Limit to 10 jobs
            item = JobItem()
            item['title'] = job.get("position")
            item['company'] = job.get("company")
            item['location'] = job.get("location") or "Remote"
            item['date_posted'] = job.get("date") or job.get("posted_at")
            item['salary'] = job.get("salary") or "N/A"
            item['source'] = "RemoteOK (Scrapy)"
            yield item
