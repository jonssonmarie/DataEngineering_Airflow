import plotly_express as px
import numpy as np
from dash import Dash, dcc, html
from dash.html import H1, Div, P, H2
from dash.dependencies import Output, Input

dropdown_options = [{"label": f"{rolls} rolls", "value": rolls } for rolls in [10, 100, 1000, 10000]]

app = Dash(__name__)

app.layout =  html.Div([html.H1("Dice Simulator"), 
                        P("Choos number of dice and number of rolls and enjoy the result"),
                        H2("number of rolls"),
                        dcc.Graph(id="dice-graph"),
                        dcc.Dropdown(id="number-rolls", options=dropdown_options, value=10),
                        H2("number of slices"),
                        dcc.Slider(id="number-dices", min=1, max=6, step=1, value=2,)
                        ])

@app.callback(
    Output("dice-graph", "figure"),
    Input("number-dices", "value"),
    Input("number-rolls", "value"),
)
def _dice_simulator_histogram(number_dices=2, number_rolls=100):
    dices = np.random.randint(1, 7, size=(number_dices, number_rolls))

    return px.histogram(dices.sum(axis=0))


if __name__ == "__main__":

    print("hello from docker side")
    app.run_server(host= "0.0.0.0", debug = True, port=8050)