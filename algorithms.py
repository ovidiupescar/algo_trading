import pandas as pd
import numpy as np
from datetime import datetime
from random import randint

class Algo:
    name = "TradingAlgorith"

    def __init__(self):
        self.d = pd.DataFrame()

    def run(self, new_entry=None):
        self.d.append(new_entry)
        self.buy_sell = randint(-100, 100)/100
        return self.buy_sell

    def __str__(self):
        return self.name

class TwoMovingAverages(Algo):
    name = "Moving Average"

    def __init__(self, window1=30, window2=100):
        self.SMAshort = pd.DataFrame()
        self.SMAlong = pd.DataFrame()
        self.window1 = window1
        self.window2 = window2
        Algo.__init__(self)

    def run(self, new_entry=None):
        self.d = self.d.append(new_entry)
        self.SMAshort = pd.DataFrame()
        self.SMAlong = pd.DataFrame()

        self.SMAshort['Adj Close'] = self.d['Adj Close'].rolling(window=self.window1).mean()
        self.SMAlong['Adj Close'] = self.d['Adj Close'].rolling(window=self.window2).mean()

        try:
            last_SMA_short = self.SMAshort.iloc[-2]['Adj Close']
            current_SMA_short = self.SMAshort.iloc[-1]['Adj Close']
            last_SMA_long = self.SMAlong.iloc[-2]['Adj Close']
            current_SMA_long = self.SMAlong.iloc[-1]['Adj Close']

            if last_SMA_short < last_SMA_long and current_SMA_short >= current_SMA_long:
                return 1
            elif last_SMA_short > last_SMA_long and current_SMA_short <= current_SMA_long:
                return -1
        except:
            pass

        return 0 



class TestAlgo(Algo):

    def __init__(self):

        self.buy_sell = 0
        self.sign = 1

    def run(self, new_entry=None):
        if self.buy_sell >= 1.0:
            self.sign = -1.0
        elif self.buy_sell <= -1.0:
            self.sign = 1.0

        self.buy_sell += self.sign * 0.1
        self.buy_sell = randint(-100, 100)/100
        return round(self.buy_sell, 2)

         