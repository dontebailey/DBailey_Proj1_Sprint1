import secrets
from pathlib import Path
from serpapi import GoogleSearch
import json
import sqlite3
from typing import Tuple


def get_data():
    page_counter = 0

    params = {  # add comment to test workflow
        "engine": "google_jobs",
        "q": "software developer",
        "google_domain": "google.com",
        "hl": "en",
        "gl": "us",
        "location": "Boston, Massachusetts, United States",
        "start": page_counter,
        "api_key": secrets.secret_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    data_results = []

    while page_counter <= 40:
        data_results.append(results.get("jobs_results"))
        page_counter += 10

    return data_results


def save_data():
    data_file = Path("data_file.json")
    data_file.write_text(json.dumps(get_data()))


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(
    company_name TEXT NOT NULL, 
    job_title TEXT NOT NULL,  
    locations TEXT NOT NULL, 
    job_description TEXT NOT NULL,
    remote TEXT NOT NULL, 
    posted_date TEXT NOT NULL, 
    salary INTEGER);''')


def main():
    conn, cursor = open_db("google_jobs_db.sqlite")
    setup_db(cursor)
    close_db(conn)


main()
