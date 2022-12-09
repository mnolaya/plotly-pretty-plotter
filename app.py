from dash import Dash, dcc, dash_table
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


if __name__ == "__main__":
    app.run_server(debug=True)