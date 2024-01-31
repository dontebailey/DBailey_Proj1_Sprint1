import secrets
from pathlib import Path
from serpapi import GoogleSearch
import json

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


