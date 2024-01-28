import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

dash.register_page(__name__, path='/evolution_item', name='Evolution by item')

df = pd.read_csv('csv/FAO_cleaned.csv', encoding='ISO-8859-1')

Year = []
Food = df.loc[df['Element'] == 'Food']
Feed = df.loc[df['Element'] == 'Feed']
for i in range(1961, 2014):
    Year.append(str(i))
df = pd.melt(df, id_vars=['Area', 'Item', 'Element'], value_vars=Year)
df = df.rename(columns={'variable': 'Year', 'value': 'Poduction'})

"""Evolutions of food & feed production by country and item"""
layout = html.Div(children=[
    html.Br(),
    html.H1('Evolution of food & feed production by country and item'),
    dcc.Dropdown(
        id='country_chosen',
        options=[{'label': i, 'value': i} for i in df['Area'].unique()],
        value='Afghanistan'
    ),
    dcc.Dropdown(
        id='item_chosen',
        options=[{'label': i, 'value': i} for i in df['Item'].unique()],
        value='Wheat and products'
    ),

    dcc.Graph(id='graph3'),
])

@dash.callback(
    output=dash.Output('graph3', 'figure'),
    inputs=[dash.Input('country_chosen', 'value'), dash.Input('item_chosen', 'value')]
)
def update_graph(country_name, item_name):
    return px.line(data_frame=df[(df['Area'] == country_name) & (df['Item'] == item_name)], x='Year', y='Poduction', color="Element", height=500, width=1000, title=f'Evolution of food production by country: {country_name} and item: {item_name}')