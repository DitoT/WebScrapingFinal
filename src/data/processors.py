import json
from collections import Counter
import pandas as pd


def clean_and_validate_jobs(jobs):

    cleaned = []

    for job in jobs:
        if not job.get("title") or not job.get("company"):
            continue

        job['title'] = job['title'].strip()
        job['company'] = job['company'].strip()
        job['location'] = job.get('location', 'Unknown').strip()
        job['salary'] = job.get('salary', 'N/A').strip()
        job['date_posted'] = job.get('date_posted', 'Unknown').strip()
        job['source'] = job.get('source', 'Unknown').strip()

        cleaned.append(job)

    return cleaned


def summarize_jobs(jobs):
    df = pd.DataFrame(jobs)
    summary = {
        "total": len(df),
        "unique_companies": df["company"].nunique(),
        "top_companies": df["company"].value_counts().head(5).to_dict(),
        "top_locations": df["location"].value_counts().head(5).to_dict(),
    }
    return summary


def export_to_csv(jobs, path):
    pd.DataFrame(jobs).to_csv(path, index=False)


def export_to_json(jobs, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)


def export_to_excel(jobs, path):
    pd.DataFrame(jobs).to_excel(path, index=False)


def load_scrapy_output(path="data_output/remoteok_scrapy_output.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Failed to load Scrapy output: {e}")
        return []