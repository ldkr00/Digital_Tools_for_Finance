### Part 1 (Binance)
# root URL for Binance API: https://api.binance.com/api/v3

# endpoint to retrieve klines for ETH/USD: /klines?symbol=ETHUSDT

# request string to retreive 75 observations of klines data for BTCUSDT since 2022-09-01
import requests
requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=75&startTime=1661990400')

# Write a function that retrieves 75 observations of klines data for a generic currency pair since a generic date. The function should take the currency pair and start date as input parameters.
def get_data(pair, date):
    url= f'https://api.binance.com/api/v3/klines?symbol={pair}&interval=1d&limit=75&startTime={date}'
    data = requests.get(url)
    #check if request worked
    assert data.status_code == 200
    return data

# Check function
data6 = get_data('BTCUSDT', 1661990400)


### Part 2 (FRED)
# root URL for FRED API: https://api.stlouisfed.org

# Endpoint to retrieve time series observations: /fred/series/observations

# Construct a query string to retrieve the series of the monthly unemployment rate (seasonally adjusted) since 2020-01. Use the fake API key abc123 in the query string.
# https://api.stlouisfed.org/fred/series/observations?api_key=abc123&series_id=UNRATE&observation_start=2020-01-01&frequency=m
