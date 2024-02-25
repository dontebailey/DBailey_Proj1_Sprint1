import sqlite3
from dash import Dash, html
import dash_ag_grid as dag
import pandas as pd

# create a connection to database
conn = sqlite3.connect("Comp490Jobs.sqlite")
data = pd.read_sql_query("Select * from jobs_listings;", conn)

app = Dash(__name__)

columnDefs = [
    {"field": "job id"},
    {"field": "job title"},
    {"field": "company name"},
    {"field": "job description"},
    {"field": "location"},
    {"field": "min-salary"},
    {"field": "max-salary"},
    {"field": "salary time"},
    {"field": "posted at"},
    {"field": "url"},
    {"field": "remote"},
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
