import dash
from dash import Dash, html, dcc
import plotly.express as px

# from index import index


# app = dash.Dash(__name__, suppress_callback_exceptions=True)
# app.layout = index

# app.layout = html.Div([
#     html.H1('Multi-page app with Dash Pages'),
#     html.Div([
#         html.Div(
#             dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
#         ) for page in dash.page_registry.values()
#     ]),
#     dash.page_container
# ])


px.defaults.template = 'plotly_white'

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]
app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=external_css)

app.layout = html.Div([
    html.Br(),
    html.H1("Dazzle Dash", className="text-center"),
    html.Div(children=[
        dcc.Link(page['name'], href=page['relative_path'], className="btn btn-primary m-2 fs-5")
        for page in dash.page_registry.values()]
        ),
    dash.page_container
], className="container")

if __name__ == '__main__':
    app.run_server(debug=True)