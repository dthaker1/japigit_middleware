# -*- coding: utf-8 -*-
from alpha_vantage.timeseries import TimeSeries


def getStockdata(symbol):
    API_KEY = '1JY2C3Z3716I4Y95'
    try:
        ts = TimeSeries(key=API_KEY, output_format='pandas')

        df,_ = ts.get_intraday(symbol,'1min')

        return str(df.tail(1).iloc[0]['4. close'])

    except Exception as e:
        return e


def main():
    outputFile = open('japi.out', 'w')
    while True:
        user_input = input("Enter the name of the symbol to get its current share price, or type QUIT to exit : \n").upper()
        if user_input.lower() != "quit":
            response = 'The current price of {} is: {}\n'.format(user_input, getStockdata(user_input))
            print(response)
            outputFile.write(response)
        else:
            raise SystemExit


main()