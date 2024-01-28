import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

dash.register_page(__name__, path='/global_evolution', name='Global Evolution')

df = pd.read_csv('csv/FAO_cleaned.csv', encoding='ISO-8859-1')

Year = []
Food = df.loc[df['Element'] == 'Food']
Feed = df.loc[df['Element'] == 'Feed']
for i in range(1961, 2014):
    Year.append(str(i))
df = pd.melt(df, id_vars=['Area', 'Item', 'Element'], value_vars=Year)
df = df.rename(columns={'variable': 'Year', 'value': 'Poduction'})
df = df.groupby(['Area', 'Year', 'Element']).sum().reset_index()


"""Total production of food & feed by country"""
layout = html.Div(children=[
    html.Br(),
    html.H1('Evolution of food & feed production by country'),
    dcc.Dropdown(
        id='country_chosen',
        options=[{'label': i, 'value': i} for i in df['Area'].unique()],
        value='Afghanistan'
    ),
    dcc.Graph(id='graph2'),
])

@dash.callback(
    output=dash.Output('graph2', 'figure'),
    inputs=[dash.Input('country_chosen', 'value')]
)
def update_graph(country_name):
    return px.line(data_frame=df[(df['Area'] == country_name)], x='Year', y='Poduction', color='Element', height=500, width=1000, title=f'Evolution of food & feed production by country: {country_name}')