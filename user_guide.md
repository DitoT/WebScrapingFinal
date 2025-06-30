User Guide
Run All Scrapers
Run the complete scraping and reporting flow: python main.py

View Output
After running, check: - data_output/jobs.db - data_output/jobs.csv - data_output/reports/report.html

Run Scrapy Spider
Runs RemoteOK Scrapy-based scraper: python src/scrapers/scrapy_crawler/run_scrapy.py

Check Scraped Record Count
Use SQLite or print statement to check count in jobs.db.