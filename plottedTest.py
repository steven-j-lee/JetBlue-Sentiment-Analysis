import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

external_stylesheets = ['style.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('tutorial/spiders/JetBlue-Data.csv')
df.head()

def plotter():
    fig = go.Figure(go.Scatter(x=df['Time'], y = df['Reception'], name = 'Perception'))
    fig.update_layout(title='JetBlue Reception over Time', plot_bgcolor='rgb(230,230,230)', showlegend = True)
    fig.show()


app.layout = html.Div([
    html.H1( 'JetBrain word frequency',
    style={'textAlign': 'center', 'margin': '48px 0'}),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Data Visualization', children=[
            html.Div([
                dcc.Graph(
                    id='plotted-graph',
                    figure = plotter()
                    ),
            ])
        ]),
        dcc.Tab(label='Improved model Visualization', children=[
            html.Div([
                html.H1("This is the content in tab 2"),
                html.P("A graph here would be nice!")
            ])
        ]),

    ],
        style={
        'fontFamily': 'system-ui'
    },
        content_style={
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'padding': '44px'
    },
        parent_style={
        'maxWidth': '1000px',
        'margin': '0 auto'
    }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
