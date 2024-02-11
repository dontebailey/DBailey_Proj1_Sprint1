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

**To create database tables and insert data into tables:**

    1st: Run the project
    2nd: After you have run the project click on google_jobs_db.sqlite file
        inside root folder to connect to database. Click test connection to make
        sure you are connected to database. Then finally click Apply and OK
    3rd: You should now have populated database tables you can view 

**About database tables:** 

I created two tables on called jobs and the other called qualifications. The jobs
table is responsible for grabbing the company name, the job title, location,
description, whether it's remote or not, date the job was posted, salary of
the job and the link to the company website. The qualifications table references
the same company name from the jobs table and grabs the job qualifications of the job posted
from that company 


**What's missing from the project:**

 1: I wasn't able to get any data for the remote section of the table
    I just didn't know what to do for that one since there was no key
    for it in the json file

2: Wasn't able to build any automated tests

3: Wasn't able to do anything with 
Continuous Integration/devOps on GitHub to run the tests



**Citing code from where I got my 
GitHub actions linter**: https://github.com/py-actions/flake8