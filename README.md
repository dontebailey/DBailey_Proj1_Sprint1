**Name:** Donte Bailey

**Install and run directions:**

1st: Make sure to set your Module SDK to
your default version of python and set
up your Virtual Environment

2nd: Import serpapi and GoogleSearch
packages using terminal in this order (

./venv/Scripts/activate.ps1

pip install python-dotenv

pip install google-search-results

)

**Project Description:** This project simply 
retrieves data from the Google Jobs API
using your API key and saves it to a 
.json file. Then saves that data from the file into
database tables

**How to Use:** You will first need to create a 
new python file and name it "secrets.py"
inside that file you will need to create
a variable name "secret_key" and for its
value you will need to put in your own
API key from SerpAPI and make sure that
the key is wrapped in quotations to make it
a string (you will need to make a SerpAPI 
account if you don't have one so you can
get your own personal API key). Then you 
should be able to run the project fine
after that

To create database tables and insert data into tables:
    You first need to uncomment in main() setup_db(cursor) and close_db(conn)
    and run the project so that you can create your database tables. After you
    have run the project comment them back out. Then inside main() uncomment get_data(cursor)
    and conn.commit() and run the project so that you can populate the tables with data and

**Citing code from where I got my 
github actions linter**: https://github.com/py-actions/flake8