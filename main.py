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

output_file = Path("output_file.json")
data_file = Path("test_data.json")

# search = GoogleSearch(params)
# results = search.get_dict()

data_results = []

# data_file.write_text(json.dumps(results.get("jobs_results")))
# while search.params_dict("start") <= 40:
while page_counter <= 40:
    data_results.append(json.loads(data_file.read_text()))
    page_counter += 10

output_file.write_text(json.dumps(data_results))


