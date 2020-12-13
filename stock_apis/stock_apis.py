import yfinance as yf
import json
import time

tickers = """AMZN FB IDXX ILMN MA PYPL SHOP SIVB DIS OKTA NTDOY NFLX ZNGA TWLO ATVI BKNG HUBS AAPL
GILD ZM BA MSFT CVS T CAH MMM TSLA ^FTSE DAX ^FCHI ^NDX ^DJI AZN.L AZN EPD PFE BTC-USD ETH-USD
CUBA ^XAU BIP BRK-B MTCH SPGI"""

tickers = indexes.split()


for ticker in tickers:
    try:
        t = yf.Ticker(ticker)
        info = t.info
        hist = t.history(period="10y")
        print(ticker)
    except:
        t = None
        print(ticker + " not found")

    if t is not None:
        with open("prices/" + ticker + ".json", "w") as f:
            json.dump(info, f, indent=4)
        hist.to_csv("prices/" + ticker + ".csv")
    time.sleep(1)