Web Scraping Final Project

This project is a fully functional job scraping system that collects job listings from multiple remote job boards using different scraping methods (static, Selenium, Scrapy), saves them to a database, performs data cleaning and analysis, and generates visual HTML reports.

Features:
    Concurrent scraping from:
        RemoteOK (Static & Scrapy)
        Remotive (Selenium)
        Jobspresso (Selenium)
    Data cleaning and validation
    Storage in SQLite database
    CSV, JSON, Excel export
    Visual reports with charts and company/location breakdowns
    CLI-ready and testable
    Modular structure with Page Object Model and Strategy Pattern

Folders:
src/: source code
data_output/: all scraped/exported data
tests/: unit tests
docs/: documentation