import pandas as pd
import dash
from dash import html, dcc
from dash_bootstrap_components import RadioItems
import plotly.express as px

dash.register_page(__name__, path='/map_item_distribution', name='Global Distribution of Items by year')

df = pd.read_csv('csv/FAO_cleaned.csv', encoding='ISO-8859-1')

Year = []
for i in range(1961, 2014):
    Year.append(str(i))
df = pd.melt(df, id_vars=['Area', 'Item', 'Element'], value_vars=Year)
df = df.rename(columns={'variable': 'Year', 'value': 'Poduction'})


"""Total production of food & feed by country"""
layout = html.Div(children=[
    html.Br(),
    html.H1('Global Distribution of Items'),
    dcc.Dropdown(
        id='item_chosen',
        options=[{'label': i, 'value': i} for i in df['Item'].unique()],
        value='Wheat and products'
    ),
    dcc.Dropdown(
        id='year_chosen',
        options=[{'label': i, 'value': i} for i in df['Year'].unique()],
        value='1961'
    ),
    RadioItems(
        options=[
            {"label": "Food", "value": 'Food'},
            {"label": "Feed", "value": 'Feed'}
        ],
        value='Food',
        id='element_chosen',
        inline=True
    ),
    dcc.Graph(id='graph5'),
])

@dash.callback(
    output=dash.Output('graph5', 'figure'),
    inputs=[dash.Input('item_chosen', 'value'), dash.Input('year_chosen', 'value'), dash.Input('element_chosen', 'value')]
)
def update_graph(item_name, year_name, element_name):
    return px.choropleth(data_frame=df[(df['Item'] == item_name) & (df['Year'] == year_name) & (df['Element'] == element_name)], locations='Area', locationmode='country names', color='Poduction', hover_name='Area', height=500, width=1000, title=f'Distribution of {item_name} in {year_name} for {element_name}')