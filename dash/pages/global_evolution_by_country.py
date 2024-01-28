import pandas as pd
import dash
from dash import html, dcc
from dash_bootstrap_components import RadioItems
import plotly.express as px

dash.register_page(__name__, path='/global_evolution_by_country', name='Global Evolution by country')

df = pd.read_csv('csv/FAO_cleaned.csv', encoding='ISO-8859-1')

"""regroup all the years columns in a column named 'Year'"""
Year = []
Food = df.loc[df['Element'] == 'Food']
Feed = df.loc[df['Element'] == 'Feed']
for i in range(1961, 2014):
    Year.append(str(i))
df = pd.melt(df, id_vars=['Area', 'Area Abbreviation', 'Item', 'Element'], value_vars=Year)
df = df.rename(columns={'variable': 'Year', 'value': 'Poduction'})
df = df.groupby(['Area', 'Year', 'Element', 'Item']).sum().reset_index()


"""Display the map of the world with the production of food by country"""
layout = html.Div(children=[
    html.Br(),
    html.H1('Evolution of food & feed production by country and for all items'),
    dcc.Dropdown(
        id='country_chosen',
        options=[{'label': i, 'value': i} for i in df['Area'].unique()],
        value='Afghanistan'
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
    dcc.Graph(id='graph4'),
])

@dash.callback(
    output=dash.Output('graph4', 'figure'),
    inputs=[dash.Input('country_chosen', 'value'), dash.Input('element_chosen', 'value')]
)
def update_graph(country_name, element_name):
    return px.line(data_frame=df[(df['Area'] == country_name) & (df['Element'] == element_name)], x='Year', y='Poduction', color='Item', height=500, width=1000, title=f'Evolution of food & feed production by country: {country_name} and element: {element_name}')