import sqlite3
from dash import Dash, html, callback, Input, Output
import dash_ag_grid as dag
import pandas as pd
import json

# create a connection to database
conn = sqlite3.connect("Comp490Jobs.sqlite")
# headline_info = pd.read_sql_query("Select job_title,company_name from jobs_listings", conn)
data = pd.read_sql_query("Select * from jobs_listings", conn)
conn.close()
app = Dash(__name__)

columnDefs = [
    # {"field": "job_id", "headerName": "Job ID"},
    {"field": "job_title", "headerName": "Job Title", "sizeToFit": True},
    {"field": "company_name", "headerName": "Company Name", "sizeToFit": True},
    # {"field": "job_description", "headerName": "Job Description"},
    {"field": "location", "headerName": "Location", "sizeToFit": True},
    # {"field": "min_salary", "headerName": "Minimum salary"},
    # {"field": "max_salary", "headerName": "Maximum salary"},
    # {"field": "salary_time", "headerName": "Salary Time"},
    # {"field": "posted_at", "headerName": "Posted"},
    # {"field": "url", "headerName": "URL"},
    # {"field": "remote", "headerName": "Remote"},
]
# Need to set columnDefs to columnDefs list of dictionaries
grid = dag.AgGrid(
    id="jobs-grid",
    rowData=data.to_dict("records"),
    columnDefs=columnDefs,
    # columnDefs=[{"field": i} for i in columnDefs],
    # columnDefs=[{"field": i} for i in headline_info.columns],
    defaultColDef={"filter": True},
    getRowId="params.data.index",
    dashGridOptions={"animateRows": False},
    columnSize="responsiveSizeToFit"
)

app.layout = html.Div([grid, html.Pre(id="pre-cell-selection-double-click-callback")])


# dcc.Textarea(readOnly=True, id="jobs_display_window", style={"width": "30%", "height": 400})

@callback(
    Output("pre-cell-selection-double-click-callback", "children"),
    Input("jobs-grid", "cellDoubleClicked"),
)
def display_cell_clicked_on(cell):
    return f"Double-clicked on cell:\n{json.dumps(cell, indent=2)}" if cell else "Double-click on a cell"


if __name__ == '__main__':
    app.run(debug=True)
