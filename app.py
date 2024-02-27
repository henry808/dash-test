# Import packages
import dash
# from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
# from dash import Input, Output, State
# from dash import dash_table 
# from dash import PreventUpdate
# import flask
from flask import Flask


def make_card(alert_message, color, cardbody, style_dict=None):
    return  html.Div([html.P("  ")    , dbc.Card([dbc.Alert(alert_message, color=color)
                        ,dbc.CardBody(cardbody)])#end card
                        ,html.P("  ")
                        ,html.P("  ")
                    ])#end div


def create_body(items):
    b = []
    for item in items:
        b.append(dbc.Col(make_card(item[0], "primary", item[1])))
    return b


def create_layout():
    layout = html.Div(style={
        'background-image': 'url("/assets/YOUR-BACKGROUND.jpg")',
        'background-position': 'center',
        }, children = [
            header
            , dbc.Container(id = 'card-cont', children = [dbc.Row(create_body(item_lists))], style = {'background-color':'white', })# end container 
            , footer
        ] #end children                     
        ) #end div
    return layout


item_lists = [["root beer" , html.A(id = 'item1', href="item link",   children=[html.Img(src="image link")])],
            ["root beer" , html.A(id = 'item2', href="item 2 link", children=[html.Img(src="image 2 link")])]
            ] # end item list

# Initialize the app - incorporate theme
# gunicorn uses this server
server = Flask(__name__)
external_stylesheets=[dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__,server = server ,meta_tags=[{ "content": "width=device-width"}], external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

# App layout
header = html.Div(dbc.Container([
            html.H1("RootbeerReport.com", className="display-3"),
            html.P("Find root beer reviews at RootbeerReport.com."),
            html.Hr(className="my-2"),
            html.P(" " " "),
            html.P(" ")
        ],  fluid=True, className="py-3",), className="p-3 bg-light rounded-3") # end container
footer = html.Div(dbc.Container([
        html.H1("RootbeerReport.com"),
        html.P(''),
        html.P("123 Fake ST NE", style= {'text-align': 'center'}),
        html.P("MN 55445", style= {'text-align': 'center'}),
        html.Hr(className="my-2"),
        html.P(''),
        html.P('Copyright © 2024 RootbeerReport - All Rights Reserved.')
    ],fluid=True, className="py-3"), className="p-3 bg-light rounded-3")  # end container


app.layout = create_layout()

# main
if __name__ == '__main__':
    app.run_server(debug=True)
