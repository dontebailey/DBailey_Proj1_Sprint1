import secrets
from pathlib import Path
from serpapi import GoogleSearch
import json

params = {
    "engine": "google_jobs",
    "q": "software developer",
    "google_domain": "google.com",
    "hl": "en",
    "gl": "us",
    "location": "Boston, Massachusetts, United States",
    "start": "0",
    "api_key": secrets.secret_key
}
data_file = Path("test_data.json")

# search = GoogleSearch(params)
# results = search.get_dict()
# data_file.write_text(json.dumps(results))

data = json.loads(data_file.read_text())
print(data)