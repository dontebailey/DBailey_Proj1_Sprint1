import sqlite3
from dash import Dash, html, callback, Input, Output, ctx, no_update
import dash_ag_grid as dag
import pandas as pd
import dash_bootstrap_components as dbc

# create a connection to database
conn = sqlite3.connect("Comp490Jobs.sqlite")
headline_info = pd.read_sql_query("Select * from jobs_listings", conn)
conn.close()
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

# Responsible for column headers
columnDefs = [
    {"field": "job_title", "headerName": "Job Title", "sizeToFit": True},
    {"field": "company_name", "headerName": "Company Name", "sizeToFit": True},
    {"field": "location", "headerName": "Location", "sizeToFit": True},
]

# Responsible for overall grid layout
grid = dag.AgGrid(
    id="jobs-grid",
    rowData=headline_info.to_dict("records"),
    columnDefs=columnDefs,
    defaultColDef={"filter": True},
    getRowId="params.data.index",
    dashGridOptions={"rowSelection": "single", "animateRows": False, "rowMultiSelectWithClick": True},
    columnSize="responsiveSizeToFit"
)
# scrollable Modal for when user clicks on a particular cell
modal = html.Div([
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Complete Job Info")),
            dbc.ModalBody(id="row-selection-modal-content", style={"white-space": "pre-wrap", "color": "black"}),
            dbc.ModalFooter(
                dbc.Button(
                    "Close",
                    id="row-selection-modal-close",
                    className="ml-auto",
                ),
            ),
        ],
        id="row-selection-modal",
        fullscreen=True,
    )
])

# Responsible for calling on my variables and laying out the overall application
app.layout = html.Div([
    grid,
    modal
])


@callback(
    Output("row-selection-modal", "is_open"),
    Output("row-selection-modal-content", "children"),
    Input("jobs-grid", "selectedRows"),
    Input("row-selection-modal-close", "n_clicks"),
)
def open_modal(selection, _):
    if ctx.triggered_id == "row-selection-modal-close":
        return False, no_update
    if selection:
        return True, [(f"Job Id: {s["job_id"]}\n"
                       f"Job Title: {s["job_title"]}\n"
                       f"Company Name: {s["company_name"]}\n"
                       f"Job Description: {s["job_description"]}\n"
                       f"Location: {s["location"]}\n"
                       f"Minimum Salary: {s["min_salary"]}\n"
                       f"Maximum Salary: {s["max_salary"]}\n"
                       f"Salary Time: {s["salary_time"]}\n"
                       f"Posted At: {s["posted_at"]}\n"
                       f"URL: {s["url"]}\n"
                       f"Remote: {s["remote"]}")
                      for s in selection]

    return no_update, no_update


if __name__ == '__main__':
    app.run(debug=True)
