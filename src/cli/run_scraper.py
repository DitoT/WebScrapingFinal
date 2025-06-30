from concurrent.futures import ThreadPoolExecutor
import time
import random
import logging


def run_all_scrapers(config):
    from src.scrapers.scraper_factory import ScraperFactory
    all_jobs = []

    def run_one(scraper_conf):
        time.sleep(random.uniform(1.5, 3.5))
        scraper = ScraperFactory.get_scraper(scraper_conf["name"])
        return scraper(limit=scraper_conf["limit"])

    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(run_one, s) for s in config["scrapers"]]
        for f in futures:
            try:
                all_jobs.extend(f.result())
            except Exception as e:
                logging.warning(f"Scraper failed: {e}")

    return all_jobs
