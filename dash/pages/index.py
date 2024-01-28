import dash
from dash import html, dcc, dash_table
import pandas as pd
import plotly.graph_objects as go

dash.register_page(__name__, path='/', name='Index')

df = pd.read_csv('csv/FAO_cleaned.csv', encoding='ISO-8859-1')

isNull = df.isnull().sum()
totalNotNull = df.notnull().sum().sum()
totalNull = df.isnull().sum().sum()
totalValue = totalNotNull + totalNull
isNull = df.isnull().sum()
col_with_null = []
col_name = []
col_value = []
for i in range(len(isNull)):
    if isNull[i] > 0:
        col_with_null.append({"Column":df.columns[i], "Missing values":isNull[i]})
        col_name.append(df.columns[i])
        col_value.append(isNull[i])


layout = html.Div([
    html.H1('Dataset information'),
    dcc.Markdown(f"""
    ### File: FAO_cleaned.csv
    #### - Columns: {len(df.columns)}
    #### - Rows: {len(df)}
    #### - Total values: {totalValue}
    #### - Missing values: {totalNull}
    #### - Not missing values: {totalNotNull}
    #### - Percentage of missing values: {round(totalNull/totalValue*100, 2)}%
    #### - Columns with missing values: {len(col_with_null)}
    #### - List of columns with missing values:

    """),
    html.Br(),
    dash_table.DataTable(columns=[{"name": i, "id": i} for i in col_with_null[0]], data=col_with_null),
], className="bg-light p-4 rounded-3")
