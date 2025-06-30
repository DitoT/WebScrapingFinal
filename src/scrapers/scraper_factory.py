from src.scrapers.static_scraper import scrape_remoteok_jobs
from src.scrapers.jobspresso_selenium_scraper import scrape_jobspresso_jobs
from src.scrapers.remotive_selenium_scraper import scrape_remotive_jobs

class ScraperFactory:
    @staticmethod
    def get_scraper(name):
        if name == "remoteok":
            return scrape_remoteok_jobs
        elif name == "jobspresso":
            return scrape_jobspresso_jobs
        elif name == "remotive-selenium":
            return scrape_remotive_jobs
        else:
            raise ValueError(f"Unknown scraper: {name}")
