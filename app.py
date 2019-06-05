import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import os

GPS = pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/OBD/master/OBD_GPS_CSV")

col_options = [dict(label=x, value=x) for x in GPS.columns]
dimensions = ["value"]

app = dash.Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])
server = app.server

app.config['suppress_callback_exceptions']=True

app.layout = html.Div(
    [
        html.H1("Visualization of both OBD and GPS by Dash"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"}
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)

@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x):
    px.set_mapbox_access_token("pk.eyJ1IjoiYmFucXVldGt1bWEiLCJhIjoiY2p0YjZ4bGJ2MGlseTN5bzlxcnlsbW8xNCJ9.udbxOpc2gZQcUX4m1VIqBg")

    return  px.scatter_mapbox(GPS,
                        lat="緯度　(°)",
                        lon="経度　(°)",
                        color=x,
                        size=x,
                        size_max=10,
                        zoom=10,
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        hover_name=x)

#plotly_expressの描画部分

if __name__ == '__main__':
    app.run_server(debug=True)
