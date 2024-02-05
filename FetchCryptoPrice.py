# Crypto price class adapted from open-sourced code on https://github.com/ertugrulaydin/python-Binance-getPrices
# Dependencies: pip install yfinance
import requests
import yfinance as yf

key = "https://api.binance.com/api/v3/ticker/price?symbol="

currencies = ["USDTTRY", "BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "AVAXUSDT", "APEUSDT", "MATICUSDT", "NEARUSDT",
              "LTCUSDT", "ICPUSDT", "MINAUSDT", "DOTUSDT", "FTTUSDT", "AXSUSDT", "SXPUSDT", "SRMUSDT", "RAYUSDT",
              "CLVUSDT", "ALGOUSDT", "CAKEUSDT", "KSMUSDT"]

class FetchPrice:

    def __init__(self, savedata):
        self.sd = savedata

    def fetchStockPrice(self, getprice):
        stock_info = yf.Ticker(getprice).info # Fetches the stock info with yahoo finance
        market_price = stock_info['regularMarketPrice']
        previous_close_price = stock_info['regularMarketPreviousClose']

        change = 100-round((100 / previous_close_price * market_price),3) # Calculates the % change in price from the previous day
        if change < 0:
            change = change+2*abs(change)
            symbol = '↑'
        else:
            change = change-2*change
            symbol = '↓'

        self.sd.print('The current price of', getprice.upper(), 'is $', end='')
        self.sd.print(market_price, symbol,'%', end='')
        self.sd.print(round(change,3))

    def fetchCryptoPrice(self, getprice):
        url = key + getprice.upper() + 'USDT'
        data = requests.get(url) # makes a request to Binance for the price
        data = data.json()
        self.sd.print("The current price of "+getprice.upper(),"is", float(data['price']), 'USD')




