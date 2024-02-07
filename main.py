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


def generate_jobs(cursor: sqlite3.Cursor):
    cursor.execute('''INSERT OR IGNORE INTO jobs VALUES 
    ('Eleven Madison Park', 'Barista','New York,NY','A three Michelin-starred restaurant','Yes','3 days ago','$24')''')


# Get 5 pages of data and save to database
def save_to_db():
    pass


def get_data():
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
            company_name = job["company_name"]
            location = job["location"]
            job_description = job["description"]
            detected_extension_posted = job["detected_extensions"]
            detected_extension_schedule = job["detected_extensions"]

            # This is the error I get when trying to get posted_date(KeyError: 'posted_at')
            # and I know I'm putting in the key right, so I commented it out for now

            # posted_date = detected_extension_posted["posted_at"]
            schedule_type = detected_extension_schedule["schedule_type"]

            # print(company_name)
            # print(location)
            print(schedule_type)


def save_data():
    data_file = Path("data_file.json")
    data_file.write_text(json.dumps(get_data()))


def main():
    # conn, cursor = open_db("google_jobs_db.sqlite")
    # setup_db(cursor)
    # generate_jobs(cursor)
    # close_db(conn)
    # save_data()
    get_data()


main()
