import pandas as pd
import dash
from dash import html, dcc, dash_table
import plotly.graph_objects as go

dash.register_page(__name__, path='/dataset', name='Dataset')

df = pd.read_csv('csv/FAO_cleaned.csv', encoding='ISO-8859-1')

Year = []
Food = df.loc[df['Element'] == 'Food']
Feed = df.loc[df['Element'] == 'Feed']
for i in range(1961, 2014):
    Year.append(str(i))
df = pd.melt(df, id_vars=['Area', 'Item', 'Element'], value_vars=Year)
df = df.rename(columns={'variable': 'Year', 'value': 'Poduction'})


layout = html.Div(children=[
    html.Br(),
    html.H1('Dataset'),
    html.Br(),
    html.Br(),
    html.H2('Filtred dataset, regroup all the years columns in a column named "Year"'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10,)
])