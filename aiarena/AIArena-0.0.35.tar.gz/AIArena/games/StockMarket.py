import requests
import json






class StockMarket:
    """This implements a game of a Stock Market Simulator"""
    def __init__(self, state=None, players=None, APIKey=None):
        #Game Constants
        self.startValue = 10**6
        self.interval = 15
        self.APIKey = APIKey

        if players is None:
            self.players = []

        if state:
            self.state = state
        else:
            self.state = {
                "endDate": "endDate",
                "symbols": ["FB"],#,"AMZN","AAPL","NFLX","GOOGL"],
                "data":{},
                "players": players,
                "portfolios":{}
            }

            for s in self.state["symbols"]:
                self.state["data"][s] = {
                    "all":{},
                    "last":{}
                }

            for p in self.players:
                self.state["portfolios"][p.id] = {
                    "cash":self.startValue,
                    "stocks":{},
                    "trades":[]
                }



    def print(self):
        print("---------------")
        for id, port in self.state["portfolios"].items():
            print(id)
            print(port['cash'])
            print(port['stocks'])
        print("---------------")

    def gatherStockData(self):
        for sym in self.state["symbols"]:
            data, last = self.getStockData(sym, str(self.interval)+"min")
            for date, value in data.items():
                self.state["data"][sym]["all"][date] = {}
                for key, val in value.items():
                    self.state["data"][sym]["all"][date][key[3:]] = float(val)
            self.state["data"][sym]["last"] = self.state["data"][sym]["all"][last]
            #print(self.state["data"][sym])

    def getStockData(self, symbol, interval):
        payload = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": interval,
            "apikey": self.APIKey
        }

        r = requests.get("https://www.alphavantage.co/query", payload)
        if r.status_code == 200:
            data = json.loads(r.content.decode())
            last = data["Meta Data"]["3. Last Refreshed"]
            return data["Time Series (" + interval + ")"], last
        else:
            print("An error occured:", r.status_code, r.content)

    def validateMove(self, move):
        pass


    def validateTrade(self, trade, portfolio):
        if trade["symbol"] in self.state["symbols"]:
            if trade["action"] == "buy":
                cost = trade["quantity"] * self.state["data"][trade["symbol"]]["last"]["close"]
                if cost < portfolio['cash']:
                    return True
            elif trade["action"] == "sell":
                if trade["symbol"] in portfolio["stocks"] and trade["quantity"] <= portfolio["stocks"][trade["symbol"]]:
                    return True
        return False

    def makeTrade(self, trade, portfolio, aid):#Assumes trade was validated
        cost = trade["quantity"] * self.state["data"][trade["symbol"]]["last"]["close"]
        if trade["action"] == "buy":
            self.state['portfolios'][aid]['cash'] -= cost
            if trade["symbol"] in portfolio:
                self.state['portfolios'][aid]['stocks'][trade["symbol"]] += trade["quantity"]
            else:
                self.state['portfolios'][aid]['stocks'][trade["symbol"]] = trade["quantity"]
        elif trade["action"] == "sell":
            self.state['portfolios'][aid]['cash'] += cost
            self.state['portfolios'][aid]['stocks'][trade["symbol"]] -= trade["quantity"]

    def makeMove(self, move):#assumes move has been validated
        for trade in move['trades']:
            portfolio = self.state['portfolios'][move['aid']]
            if self.validateTrade(trade, portfolio):
                self.makeTrade(trade,portfolio,move['aid'])


    def postMove(self):
        pass

    def endGame(self, winner):
        #print("Winner", winner)
        #print(self.state["players"][winner])
        self.state["Winner"] = winner

import AIArena



if __name__ == "__main__":
    class lilStockBuddy(AIArena.AI):  # <2>
        def __init__(self, name):
            super().__init__(name, "StockMarket")

    ai1 = lilStockBuddy("lilStockBuddy")
    #sm = StockMarket(players=[ai1],APIKey="0C0G6TQ153Q7Y67L")
    sm = StockMarket(players=[ai1], APIKey="0C0G6TQ153Q7Y67L")
    sm.gatherStockData()


    """
    trades = [
        {'action':"buy",'symbol':"FB",'quantity':100}
    ]

    move = {
        'aid': ai1.id,
        'trades': trades
    }

    sm.print()
    sm.makeMove(move)
    sm.print()

    trades = [
        {'action': "sell", 'symbol': "FB", 'quantity': 100},
        {'action': "buy", 'symbol': "FB", 'quantity': 1000},
        {'action': "sell", 'symbol': "FB", 'quantity': 100}
    ]

    move = {
        'aid': ai1.id,
        'trades': trades
    }

    sm.makeMove(move)
    sm.print()
    """