import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import os
#from bottle import route, run
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

OBD2=pd.read_csv("https://raw.githubusercontent.com/BanquetKuma/OBD/master/OBD_GPS_CSV")

col_options = [dict(label=x, value=x) for x in OBD2.columns]
dimensions = ["x", "y", "color"]

app = dash.Dash(__name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])
server = app.server

app.layout = html.Div(
    [
        html.H1("Visualization of OBD by Dash"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"})
    ])

@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color):
    return px.scatter(
        OBD2,
        x=x,
        y=y,
        color=color,
        height=700)

#plotly_expressの描画部分
if __name__ == '__main__':
    app.run_server(debug=True)

#run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
