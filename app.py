from dash import Dash, dcc, dash_table
import dash_bootstrap_components as dbc

from pages.sidebar import sidebar

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(sidebar)
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)