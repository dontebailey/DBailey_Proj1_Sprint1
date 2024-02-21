**Name:** _Donte Bailey_

**Install and run directions:**

**1st**: Make sure to set your Module SDK to
your default version of python and set
up your Virtual Environment

**2nd**: There is a requirements.txt file that contains all the packages that need to be
installed. When you first open the project in your IDE it should prompt you in the corner
of your screen to install all packages in requirements.txt. **Click install** for all necessary
packages to run program

**3rd:** *Last package to install through IDE:* install package **google-search-results** 
in File->Settings->Python Interpreter. Click the + button and search up the package 
and install the latest version


**Project Description:** This project simply 
retrieves data from two separate datasets (Google Jobs API and Sprint3Data.xlsx) 
and inserts both datasets into a database table


**How to Use:** You will first need to create a 
new python file and name it "secrets.py"
inside that file you will need to create
a variable name "secret_key" and for its
value you will need to put in your own
API key from SerpAPI and make sure that
the key is wrapped in quotations to make it
a string (you will need to make a SerpAPI 
account if you don't have one, so you can
get your own personal API key). Then you 
should be able to run the project fine
after that

**To create database tables and insert data into tables:**

    1st: Run the project
    2nd: After you have run the project click on Comp490Jobs.sqlite file
        inside root folder to connect to database. Click test connection to make
        sure you are connected to database. Then finally click Apply and OK
    3rd: You should now have populated database tables you can view 

**About database tables:** 

This table is the combined jobs from the Google Jobs API and Sprint3Data.xlsx.
For each individual job listed you should be able to see its specific job id,job title,
company name,job description, location, minimum salary, maximum salary, salary type, time
when post was created, the url of job, whether the job is remote. There are default values
for when a certain column isn't available for a specific job


**What's missing from the project:**

 1: My automated tests for sprint3

2: GitHub Actions linter fails


