import sqlite3
from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

# create a connection to database
conn = sqlite3.connect("Comp490Jobs.sqlite")
data = pd.read_sql_query("Select * from jobs_listings", conn)
conn.close()
app = Dash(__name__)

columnDefs = [
    {"field": "job_id", "headerName": "Job Id"},
    {"field": "job_title", "headerName": "Job Title"},
    {"field": "company_name", "headerName": "Company Name"},
    {"field": "job_description", "headerName": "Job Description"},
    {"field": "location", "headerName": "Location"},
    {"field": "min_salary", "headerName": "Minimum salary"},
    {"field": "max_salary", "headerName": "Maximum salary"},
    {"field": "salary_time", "headerName": "Salary Time"},
    {"field": "posted_at", "headerName": "Posted"},
    {"field": "url", "headerName": "URL"},
    {"field": "remote", "headerName": "Remote"},
]

grid = dag.AgGrid(
    id="jobs-grid",
    rowData=data.to_dict("records"),
    columnDefs=columnDefs
)

app.layout = html.Div([
    # dcc.Textarea(readOnly=True, id="jobs_display_window", style={"width": "30%", "height": 400})
    grid
])

if __name__ == '__main__':
    app.run(debug=True)
