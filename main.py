import dash
import datetime
from dash.dependencies import Input, Output
import pandas_datareader as web
import dash_core_components as dcc
import dash_html_components as html

from reader import get_df

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()

stock = 'TSLA'

df = web.DataReader(stock, 'yahoo', start, end)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Stocks'),
    html.Br(),
    html.Span(children='Stock  '),
    dcc.Input(id='stock', value='', type='text'),
    html.Br(), html.Br(),
    html.Span(children='Year  '),
    dcc.Input(id='year', value='', type='text'),
    html.Br(), html.Br(),
    html.Span(children='Month  '),
    dcc.Input(id='month', value='', type='text'),
    html.Br(), html.Br(),
    html.Span(children='Day  '),
    dcc.Input(id='day', value='', type='text'),
    html.Br(), html.Br(),
    html.Div(id='graph')
])

@app.callback(
    Output(component_id='graph', component_property='children'), [
        Input(component_id='stock', component_property='value'),
        Input(component_id='year', component_property='value'),
        Input(component_id='month', component_property='value'),
        Input(component_id='day', component_property='value')
     ]
)
def get_graph(stock, year, month, day):
    try:
        df = get_df(stock, int(year), int(month), int(day))
        return dcc.Graph(
            id='stock_graph',
            figure={
                'data': [
                    {'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock}
                ],
                'layout': {
                    'title': f'Stock Growth of {stock} from {year}/{month}/{day} to today!'
                }
            }
        )
    except Exception as e:
        return 'Something went wrong. ' + str(e)


if __name__ == '__main__':
    app.run_server(debug=True)
