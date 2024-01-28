import secrets
from serpapi import GoogleSearch

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

search = GoogleSearch(params)
results = search.get_dict()

