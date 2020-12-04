import pandas as pd
import numpy as np
from datetime import datetime
from random import randint

class Algo:
    name = "TradingAlgorith"

    def __init__(self, d):
        self.d = d

    def run(self):
        self.buy_sell = randint(-100, 100)/100
        return self.buy_sell

    def __str__(self):
        return self.name

class TwoMovingAverages(Algo):
    name = "Moving Average"

    def __init__(self, t)
    def run(self):
        self.buy_sell = randint(-100, 100)
        return self.buy_sell 
