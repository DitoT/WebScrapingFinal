import pytest
from src.scrapers.static_scraper import scrape_remoteok_jobs

def test_scrape_remoteok_returns_list():
    jobs = scrape_remoteok_jobs(limit=3)
    assert isinstance(jobs, list)
    assert len(jobs) <= 3

def test_scraped_jobs_have_required_fields():
    jobs = scrape_remoteok_jobs(limit=1)
    if jobs:
        job = jobs[0]
        for field in ['title', 'company', 'location', 'date_posted', 'salary', 'source']:
            assert field in job
