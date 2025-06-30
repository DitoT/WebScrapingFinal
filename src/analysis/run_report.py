import sqlite3
import pandas as pd
import json

from src.analysis.generate_report import summarize_jobs, create_charts, generate_html_report

def load_jobs_from_db(db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM jobs", conn)
    conn.close()
    return df.to_dict(orient="records")

if __name__ == "__main__":
    jobs = load_jobs_from_db("data_output/jobs.db")
    summary = summarize_jobs(jobs)
    create_charts(jobs)
    generate_html_report(jobs, summary)
    print("Report generated: data_output/reports/report.html")
