import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def summarize_jobs(jobs):
    df = pd.DataFrame(jobs)
    return {
        "total": len(df),
        "unique_companies": df["company"].nunique(),
        "top_companies": df["company"].value_counts().head(5).to_dict(),
        "top_locations": df["location"].value_counts().head(5).to_dict()
    }


def create_charts(jobs):
    df = pd.DataFrame(jobs)
    os.makedirs("data_output/reports", exist_ok=True)

    # Chart 1: Jobs by Source
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='source')
    plt.title("Jobs by Source")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("data_output/reports/jobs_by_source.png")
    plt.close()

    # Chart 2: Top Hiring Companies
    top_companies = df['company'].value_counts().head(5)
    plt.figure(figsize=(8, 6))  # bigger for readability
    top_companies.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.ylabel('')
    plt.title("Top Hiring Companies")
    plt.tight_layout()
    plt.savefig("data_output/reports/top_companies.png")
    plt.close()



def generate_html_report(jobs, summary):
    html = "<html><head><meta charset='UTF-8'> <title>Job Report</title> </head><body>"
    html += "<h1> Job Scraping Summary</h1>"
    html += f"<p>Total Jobs: {summary['total']}</p>"
    html += f"<p>Unique Companies: {summary['unique_companies']}</p>"

    html += "<h2>Top Companies</h2><ul>"
    for company, count in summary['top_companies'].items():
        html += f"<li>{company}: {count}</li>"
    html += "</ul>"

    html += "<h2>Top Locations</h2><ul>"
    for loc, count in summary['top_locations'].items():
        html += f"<li>{loc}: {count}</li>"
    html += "</ul>"

    html += "<h2>Charts</h2>"
    html += "<img src='jobs_by_source.png'><br>"
    html += "<img src='top_companies.png'><br>"

    html += "</body></html>"

    with open("data_output/reports/report.html", "w", encoding="utf-8") as f:
        f.write(html)

