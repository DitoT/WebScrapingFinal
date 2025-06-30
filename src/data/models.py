import sqlite3

def save_jobs_to_db(jobs, db_path="data_output/jobs.db"):
    conn = sqlite3.connect("data_output/jobs.db")
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, date_posted, salary, source)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            job.get("title"),
            job.get("company"),
            job.get("location"),
            job.get("date_posted"),
            job.get("salary"),
            job.get("source")
        ))

    conn.commit()
    conn.close()
