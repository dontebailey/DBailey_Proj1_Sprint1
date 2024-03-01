import sqlite3
from dash import Dash, html, callback, Input, Output, ctx, no_update
import dash_ag_grid as dag
import pandas as pd
import json
import dash_bootstrap_components as dbc

# create a connection to database
conn = sqlite3.connect("Comp490Jobs.sqlite")
# headline_info = pd.read_sql_query("Select job_title,company_name from jobs_listings", conn)
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
            dbc.ModalHeader(dbc.ModalTitle("More information about selected row")),
            dbc.ModalBody(id="row-selection-modal-content"),
            dbc.ModalFooter(
                dbc.Button(
                    "Close",
                    id="row-selection-modal-close",
                    className="ml-auto",
                ),
            ),
        ],
        id="row-selection-modal",
        # scrollable=True,
        # is_open=False,
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
# def display_cell_clicked_on(cell):
#     return f"Double-clicked on cell:\n{json.dumps(cell, indent=2)}" if cell else "Double-click on a cell"
def open_modal(selection, _):
    if ctx.triggered_id == "row-selection-modal-close":
        return False, no_update
    if selection:
        return True, "You selected " + ", ".join(
            [
                f"{s['job_title']}  {s['company_name']}  {s['location']})"
                for s in selection
            ]
        )

    return no_update, no_update


if __name__ == '__main__':
    app.run(debug=True)
