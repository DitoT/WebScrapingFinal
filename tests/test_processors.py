import pytest

from src.data.processors import clean_and_validate_jobs


def test_clean_and_validate_jobs_valid():
    jobs = [
        {"title": "Developer", "company": "Acme", "location": "Remote", "salary": "100k", "date_posted": "Today", "source": "Test"}
    ]
    cleaned = clean_and_validate_jobs(jobs)
    assert len(cleaned) == 1
    assert cleaned[0]["title"] == "Developer"
    assert cleaned[0]["company"] == "Acme"
    assert cleaned[0]["location"] == "Remote"
    assert cleaned[0]["source"] == "Test"


def test_clean_and_validate_jobs_missing_fields():
    jobs = [{"title": None, "company": None}]
    cleaned = clean_and_validate_jobs(jobs)
    assert cleaned == []
