import secrets
from pathlib import Path
from serpapi import GoogleSearch
import json
import sqlite3
from typing import Tuple


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs(
    company_name TEXT NOT NULL PRIMARY KEY , 
    job_title TEXT NOT NULL,  
    locations TEXT NOT NULL, 
    job_description TEXT NOT NULL,
    remote TEXT NOT NULL, 
    posted_date TEXT NOT NULL, 
    salary TEXT NOT NULL, 
    link TEXT NOT NULL);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS qualifications(
    company TEXT NOT NULL,
    job_qualifications TEXT NOT NULL PRIMARY KEY ,
    FOREIGN KEY(company) REFERENCES jobs(company_name)
    );''')


def insert_job(cursor: sqlite3.Cursor, company_name, job_title, locations, job_description,
               remote, posted_date, salary, link):
    cursor.execute('''INSERT OR IGNORE INTO jobs (company_name, job_title, locations,job_description,
    remote,posted_date,salary,link) VALUES(?,?,?,?,?,?,?,?)''', (company_name, job_title, locations,
                                                                 job_description, remote, posted_date, salary, link
                                                                 ))


def insert_qualifications(cursor: sqlite3.Cursor, company, job_qualifications):
    cursor.execute('''INSERT OR IGNORE INTO qualifications(company, job_qualifications) VALUES (?,?)''',
                   (company, job_qualifications))


def get_data(cursor: sqlite3.Cursor):
    page_counter = 0

    params = {
        "engine": "google_jobs",
        "q": "software developer",
        "google_domain": "google.com",
        "hl": "en",
        "gl": "us",
        "location": "Boston, Massachusetts, United States",
        "start": page_counter,
        "api_key": secrets.secret_key
    }

    data_file = Path("data_file.json")

    search = GoogleSearch(params)
    results = search.get_dict()

    data_results = []

    while page_counter <= 40:
        data_results.append(results.get("jobs_results"))
        page_counter += 10

    data_file.write_text(json.dumps(data_results))

    data = json.loads(Path("data_file.json").read_text())

    for page in data:
        for job in page:
            company_name = job.get("company_name", "")
            job_title = job.get("title", "")
            location = job.get("location", "")
            job_description = job.get("description")
            detected_extension = job.get("detected_extensions", {})
            related_link = job.get("related_links", "")
            posted_date = detected_extension.get("posted_at", "")
            salary = detected_extension.get("salary", "")
            company_link = related_link[0].get("link", "")
            job_highlights = job.get("job_highlights", [])
            # items is the name of the key where the put the qualifications list inside the .json file
            array_counter = 0
            items = job_highlights[array_counter].get("items", [])
            insert_job(cursor, company_name, job_title, location, job_description,
                       False, posted_date, salary, company_link)
            for each_item in items:
                if array_counter <= len(items):
                    array_counter += 1
                    insert_qualifications(cursor, company_name, each_item)


def main():
    conn, cursor = open_db("google_jobs_db.sqlite")
    setup_db(cursor)
    get_data(cursor)
    conn.commit()
    close_db(conn)


main()
