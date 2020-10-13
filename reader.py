import pandas_datareader as web
import datetime


def get_df(stock, year, month, day):
    start = datetime.datetime(year, month, day)
    end = datetime.datetime.now()
    df = web.DataReader(stock, 'yahoo', start, end)
    return df