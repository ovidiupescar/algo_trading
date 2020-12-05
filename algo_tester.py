from algorithms import TwoMovingAverages, TestAlgo
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

COMMISSION = 0.99 # 1%
INVESTMENT = 10000


class AlgoTester():

    def __init__(self, dataset_path, algo, investment):
        """receives the dataset path and the algorithm that you want to test"""
        self.ticker = dataset_path.split('/')[1].split('.')[0]
        self.initial_investment = investment
        self.cash = investment
        self.dataset = pd.read_csv(dataset_path)
        self.algo = algo
        self.inv = False
        self.stocks = 0

    def run(self):
        """ for each row in the dataframe, applies the algo, gets the buy/sell rating, plots a graph and return the dataset """
        self.buy_sell = []
        self.order = []
        self.investment = []
        self.variation = []
        self.sell = []
        self.buy = []

        
        def apply_algo(row):
            """function that applies the algorithm to each dataframe row"""
            current_buy_sell = self.algo.run(row)
            self.build_confidence(current_buy_sell, row['Adj Close'])

        self.dataset.apply(
            lambda row:
                apply_algo(row),
            axis=1
        )

        self.dataset["buy_sell"] = self.buy_sell
        self.add_all_to_dataset()
        print(self.dataset)
        self.prepare_report()
        self.plot_diagram()
        return self.dataset

    def add_all_to_dataset(self):
        self.dataset['buy_sell'] = self.buy_sell
        self.dataset['investment'] = self.investment
        self.dataset['sell'] = self.sell
        self.dataset['buy'] = self.buy
        self.dataset['variation'] = self.variation

    def build_confidence(self, current_buy_sell, price):
        self.buy_sell.append(current_buy_sell)

        bs = 0

        if self.inv:
            if current_buy_sell < -0.5:
                bs = self.sell_order(price)
        else:
            if current_buy_sell > 0.5:
                bs = self.buy_order(price)

        if bs == 1:
            self.buy.append(price)
            self.sell.append(np.nan)
        elif bs == -1:
            self.buy.append(np.nan)
            self.sell.append(price)
        else:
            self.buy.append(np.nan)
            self.sell.append(np.nan)
     
        current_val = self.cash
        if self.inv:
            current_val = self.stocks * price
        current_variation = current_val/self.initial_investment - 1
        
        self.order.append(bs)
        self.investment.append(current_val)
        self.variation.append(current_variation)

    def buy_order(self, price):
        self.stocks = (self.cash * COMMISSION) / price
        self.cash = 0
        self.inv = True
        return 1

    def sell_order(self, price):
        self.cash = self.stocks * price * COMMISSION
        self.stocks = 0
        self.inv = False
        return -1

    def plot_diagram(self):
        dt = self.dataset
        plt.figure(figsize=(12.5, 4.5))
        plt.plot(dt['Adj Close'], label=self.ticker, alpha=0.35)
        #plt.plot(dt['investment'], label="investment")
        #plt.plot(dt['variation'], label="variation")
        plt.scatter(dt.index, dt['buy'], label='Buy', marker='^', color='green')
        plt.scatter(dt.index, dt['sell'], label='Sell', marker='v', color='red')
        plt.title("Istoricul {}".format(self.ticker))
        plt.xlabel('perioada')
        plt.ylabel('Pretul final de zi ($)')
        plt.legend(loc='upper left')
        
        plt.show()
    
    def prepare_report(self):
       print("Investment: {}".format(self.initial_investment))
       print("Current Cash: {}".format(self.investment[-1]))
       print("Variation: {}".format(self.variation[-1]))      



a = TwoMovingAverages(10, 80)
t = AlgoTester(dataset_path="prices/NFLX.csv", algo=a, investment=INVESTMENT)

t.run()

