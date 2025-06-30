Technical Architecture (Overview)
Project Layers
Scraper Layer

Static Scraper: RemoteOK
Selenium Scrapers: Remotive, Jobspresso
Scrapy Spider: RemoteOK
Managed using Strategy Pattern via run_scraper.py
Pipeline

Collected jobs go through clean_and_validate_jobs()
Jobs are saved in SQLite via database.py
Uses a unified job model
Export and Reporting

Exports to CSV, JSON, Excel
Charts and HTML report generated using matplotlib and seaborn
Concurrency

Parallel scraping using ThreadPoolExecutor
Patterns Used

Strategy Pattern: select scraper by name
Factory Pattern: ScraperFactory
Observer Pattern (Optional): Logging and output tracking
Testing

test_processors.py ensures data cleaning logic
Easily extensible to test scraper outputs
Config & Extensibility
Uses settings.yaml to define scraper sources and limits
Easily extensible by adding new scraper classes to the strategy map
