import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

dash.register_page(__name__, path='/distribution', name='Distribution')

df = pd.read_csv('csv/FAO_cleaned.csv', encoding='ISO-8859-1')

"""columns is a list in int"""
columuns = [{'label': col, 'value': col} for col in df.columns if col.isnumeric()]

layout = html.Div(children=[
    html.Br(),
    html.H1('Global Distribution for a selected year'),
    dcc.Dropdown(
        id='col_chosen',
        options=columuns,
        value='1961'
    ),
    dcc.Graph(id='graph1'),
])

@dash.callback(
    output=dash.Output('graph1', 'figure'),
    inputs=dash.Input('col_chosen', 'value')
)
def update_graph(col_name):
    return px.histogram(data_frame=df, x=col_name, y='Element', height=500, width=1000, title=f'Distribution of {col_name}')