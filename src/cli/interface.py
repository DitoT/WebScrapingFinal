import click
from src.scrapers.static_scraper import scrape_indeed_jobs, scrape_remoteok_jobs, scrape_wwr_jobs
from src.scrapers.selenium_scraper import scrape_indeed_dynamic
from src.data.models import save_jobs_to_db
from src.data.database import init_db
from src.data.processors import clean_and_validate_jobs

import csv
import json

@click.command()
@click.option('--source', '-s', multiple=True, type=click.Choice(['indeed', 'remoteok', 'wwr', 'indeed-selenium'], case_sensitive=False),
              help='Choose which sources to scrape')
@click.option('--limit', '-l', default=5, help='Number of jobs per source to fetch')
@click.option('--csv', 'csv_path', default=None, help='Export results to CSV')
@click.option('--json', 'json_path', default=None, help='Export results to JSON')
def run_cli(source, limit, csv_path, json_path):
    """
    Run job scrapers with custom options.
    """
    init_db()
    all_jobs = []

    if not source:
        click.echo("⚠️  No source specified. Use --source to specify at least one.")
        return

    for src in source:
        click.echo(f"🔍 Scraping from {src} with limit={limit}...")

        if src == 'indeed':
            jobs = scrape_indeed_jobs(limit=limit)
        elif src == 'indeed-selenium':
            jobs = scrape_indeed_dynamic(limit=limit)
        elif src == 'remoteok':
            jobs = scrape_remoteok_jobs(limit=limit)
        elif src == 'wwr':
            jobs = scrape_wwr_jobs(limit=limit)
        else:
            click.echo(f"❌ Unknown source: {src}")
            continue

        cleaned = clean_and_validate_jobs(jobs)
        all_jobs.extend(cleaned)

        click.echo(f"✅ {src}: {len(cleaned)} jobs collected.")

    if all_jobs:
        save_jobs_to_db(all_jobs)
        click.echo(f"💾 {len(all_jobs)} jobs saved to database.")

        if csv_path:
            export_to_csv(all_jobs, csv_path)
            click.echo(f"📁 Data exported to CSV: {csv_path}")

        if json_path:
            export_to_json(all_jobs, json_path)
            click.echo(f"📁 Data exported to JSON: {json_path}")
    else:
        click.echo("⚠️ No jobs collected.")

def export_to_csv(jobs, path):
    keys = jobs[0].keys()
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(jobs)

def export_to_json(jobs, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(jobs, f, indent=2)
