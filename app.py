import dash
from dash.dependencies import Input, Output

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)

app.layout = html.Div([
        html.H1("Dashboard title",
                style={"text-align": "center", "fontSize": "50px",
                       "margin": "0"}),

        dcc.Checklist(id="input_1", value=[1], options=[
            {"label": "Hello", "value": 1},
            {"label": "World", "value": 2}],
                      style={"width": "10%", "position": "absolute",
                             "display": "grid", "left": "10%", "top": "25%",
                             "height": "12%"}),

        dcc.RadioItems(id="input_2", options=[
            {"label": "This", "value": 1},
            {"label": "is a", "value": 2},
            {"label": "simple", "value": 3},
            {"label": "dashboard", "value": 4}], value=2,
                       style={"width": "10%", "position": "absolute",
                              "display": "grid", "left": "60%", "top": "25%",
                              "height": "12%"}),

        dcc.Graph(
            style={"width": "40%", "height": "50%", "position": "absolute",
                   "left": "10%", "top": "40%"}, id="output_1", figure={}),

        html.Div(id="output_2", children=[],
                 style={"top": "50%", "left": "60%", "position": "absolute",
                        "border": "black solid 2px", "padding": "4px"})
    ], style={"backgroundColor": "#F1F1F1", "height": "100vh"})


@app.callback(
     [Output(component_id='output_1', component_property='figure'),
      Output(component_id='output_2', component_property='children')],

     [Input(component_id='input_1', component_property='value'),
      Input(component_id='input_2', component_property='value')]
)
def update_graphs(backend_input1, backend_input2):
    plot = make_subplots()

    if 1 in backend_input1:
        plot.add_trace(go.Scatter(x=[1, 2], y=[3, 4]))

    if 2 in backend_input1:
        plot.add_trace(go.Scatter(x=[1, 2], y=[4, 3],
                                  marker=dict(color="black")))

    backend_output2 = backend_input2

    return [plot, backend_output2]


if __name__ == '__main__':
    app.run_server(debug=True, port=1234)
