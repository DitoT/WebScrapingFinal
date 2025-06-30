# API Reference

This document describes the key modules and functions in the project.

---

## main.py
- Entry point of the application.
- Runs all scrapers, performs validation, saves to DB, exports files, and generates report.

---

## src/cli/run_scraper.py
- `run_all_scrapers(config)`: Executes all scraper strategies concurrently using ThreadPoolExecutor.

---

## src/utils/config.py
- `load_config()`: Loads YAML configuration for scraper setup and output paths.

---

## src/data/database.py
- `init_db()`: Initializes the SQLite database with the jobs table.
- `save_jobs_to_db(jobs)`: Inserts validated jobs into the database.

---

## src/data/processors.py
- `clean_and_validate_jobs(jobs)`: Removes incomplete entries and normalizes job fields.
- `summarize_jobs(jobs)`: Generates a summary dictionary (total jobs, top companies/locations).
- `export_to_csv(jobs, path)`: Exports cleaned jobs to CSV.
- `export_to_json(jobs, path)`: Exports cleaned jobs to JSON.
- `export_to_excel(jobs, path)`: Exports cleaned jobs to Excel.
- `load_scrapy_output(path)`: Loads Scrapy-generated JSON jobs and appends source field.

---

## src/analysis/generate_report.py
- `create_charts(jobs)`: Creates PNG charts from job data using matplotlib.
- `generate_html_report(jobs, summary)`: Builds and saves the report.html file with stats and embedded charts.

---

## src/scrapers/
- `remoteok_static_scraper.py`: Static scraping of RemoteOK.
- `remotive_selenium_scraper.py`: Selenium scraper for Remotive.
- `jobspresso_selenium_scraper.py`: Selenium scraper for Jobspresso.
- `scrapy_crawler/remoteok_spider.py`: Scrapy spider for RemoteOK.
- `run_scrapy.py`: Runs the Scrapy spider and saves JSON output.

---

## tests/test_processors.py
- Unit tests for `clean_and_validate_jobs()` using pytest.

---

All modules follow a modular structure and are integrated in `main.py` via config.
