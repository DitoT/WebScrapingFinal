import os
from src.utils.config import load_config
from src.cli.run_scraper import run_all_scrapers
from src.data.database import init_db
from src.data.models import save_jobs_to_db
from src.data.processors import (
    clean_and_validate_jobs,
    summarize_jobs,
    export_to_csv,
    export_to_json,
    export_to_excel
)
from src.analysis.generate_report import (
    create_charts,
    generate_html_report
)
import json

def load_scrapy_output(path="data_output/remoteok_scrapy_output.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            jobs = json.load(f)
            # Ensure all jobs have 'source' field
            for job in jobs:
                job["source"] = job.get("source", "RemoteOK (Scrapy)")
            return jobs
    except Exception as e:
        print(f"⚠️ Failed to load Scrapy output: {e}")
        return []

def main():
    # Load YAML config
    config = load_config()

    # Step 1: Init DB
    init_db()

    # Step 2: Run scrapers in parallel
    print("Running scrapers...")
    all_jobs = run_all_scrapers(config)
    # Load Scrapy jobs from JSON
    scrapy_jobs = load_scrapy_output("data_output/remoteok_scrapy_output.json")
    print(f"🕷️ Loaded {len(scrapy_jobs)} jobs from RemoteOK (Scrapy)")
    all_jobs.extend(scrapy_jobs)

    if not all_jobs:
        print("⚠️ No jobs scraped. Exiting.")
        return
    import subprocess
    subprocess.run(["python", "src/scrapers/scrapy_crawler/run_scrapy.py"])

    # Step 3: Clean and validate
    print(f"Scraped {len(all_jobs)} raw jobs")
    jobs = clean_and_validate_jobs(all_jobs)
    print(f"Validated {len(jobs)} jobs")

    # Step 4: Save to DB
    save_jobs_to_db(jobs)

    # Step 5: Export data
    export_to_csv(jobs, config["storage"]["export_csv"])
    export_to_json(jobs, config["storage"]["export_json"])
    export_to_excel(jobs, config["storage"]["export_excel"])

    # Step 6: Analyze & report
    summary = summarize_jobs(jobs)
    create_charts(jobs)
    generate_html_report(jobs, summary)

    print("🎉 All done! Report generated at: data_output/reports/report.html")

if __name__ == "__main__":
    os.makedirs("data_output/reports", exist_ok=True)
    main()
