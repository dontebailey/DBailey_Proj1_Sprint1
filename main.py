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
    salary TEXT);''')


def insert_job(cursor: sqlite3.Cursor, company, job_title, locations, job_description,
               remote, posted_date, salary):
    cursor.execute('''INSERT OR IGNORE INTO jobs (company_name, job_title, locations,job_description,
    remote,posted_date,salary) VALUES(?,?,?,?,?,?,?)''', (company, job_title, locations,
                                                          job_description, remote, posted_date, salary
                                                          ))


def get_data(cursor: sqlite3.Cursor):
    # page_counter = 0
    #
    # params = {  # add comment to test workflow
    #     "engine": "google_jobs",
    #     "q": "software developer",
    #     "google_domain": "google.com",
    #     "hl": "en",
    #     "gl": "us",
    #     "location": "Boston, Massachusetts, United States",
    #     "start": page_counter,
    #     "api_key": secrets.secret_key
    # }
    #
    # search = GoogleSearch(params)
    # results = search.get_dict()
    #
    # data_results = []
    #
    # while page_counter <= 40:
    #     data_results.append(results.get("jobs_results"))
    #     page_counter += 10
    #
    # return data_results

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

    # search = GoogleSearch(params)
    # results = search.get_dict()
    #
    # data_results = []
    #
    # while page_counter <= 40:
    #     data_results.append(results.get("jobs_results"))
    #     page_counter += 10

    # data_file.write_text(json.dumps(data_results))

    # opening json file
    # file = open("data_file.json")

    # returns JSON object as a dictionary
    # data = json.loads(Path("data_file.json").read_text())

    data = json.loads(data_file.read_text())

    for page in data:
        for job in page:
            company_name = job.get("company_name", "")
            job_title = job.get("title", "")
            location = job.get("location", "")
            job_description = job.get("description")
            detected_extension = job.get("detected_extensions", {})
            posted_date = detected_extension.get("posted_at", "None")
            salary = detected_extension.get("salary", "")

            insert_job(cursor, company_name, job_title, location, job_description,
                       False, posted_date, salary)


def save_data(cursor:sqlite3.Cursor):
    data_file = Path("data_file.json")
    data_file.write_text(json.dumps(get_data(cursor)))


def main():
    conn, cursor = open_db("google_jobs_db.sqlite")
    # setup_db(cursor)
    # insert_job(cursor)
    # close_db(conn)

    get_data(cursor)
    # save_data(cursor)
    conn.commit()

main()
