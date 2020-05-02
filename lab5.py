import requests as rq
import time

def price_data():
        ETH = rq.get("https://bitbay.net/API/Public/ETH/ticker.json")
        BTC = rq.get("https://bitbay.net/API/Public/BTC/ticker.json")
        LTC = rq.get("https://bitbay.net/API/Public/LTC/ticker.json")
        BCC = rq.get("https://bitbay.net/API/Public/BCC/ticker.json")
        GAME = rq.get("https://bitbay.net/API/Public/GAME/ticker.json")
        return ETH.json(), BTC.json(), LTC.json(), BCC.json(), GAME.json()

def maximal_profit(amount):
    while True:
        ETH_ticker, BTC_ticker, LTC_ticker, BCC_ticker, GAME_ticker = price_data()

        price_differences = {
            'ETH': (ETH_ticker['max']) / float(ETH_ticker['min']) - 1,
            'BTC': float(BTC_ticker['max']) / float(BTC_ticker['min']) - 1,
            'LTC': float(LTC_ticker['max']) / float(LTC_ticker['min']) - 1,
            'BCC': float(BCC_ticker['max']) / float(BCC_ticker['min']) - 1,
            'GAME': float(GAME_ticker['max']) / float(GAME_ticker['min']) - 1}

        volumes = { 'ETH': float(ETH_ticker['volume']),
            'BTC': float(BTC_ticker['volume']),
            'LTC': float(LTC_ticker['volume']),
            'BCC': float(BCC_ticker['volume']),
            'GAME': float(GAME_ticker['volume'])}

        lowest_price = {'ETH': float(ETH_ticker['min']),
            'BTC': float(BTC_ticker['min']),
            'LTC': float(LTC_ticker['min']),
            'BCC': float(BCC_ticker['min']),
            'GAME': float(GAME_ticker['min'])}

        sorted_cryptocurrency = sorted(price_differences, key=price_differences.get, reverse=True)

        for cryptocurrency in sorted_cryptocurrency:
            print(cryptocurrency, price_differences[cryptocurrency] * 100)

        for cryptocurrency in sorted_cryptocurrency:
            if amount > 0:
                if volumes[cryptocurrency] * lowest_price[cryptocurrency] < amount:
                    amount = amount - \
                             volumes[cryptocurrency] * lowest_price[cryptocurrency]
                    print('You can buy:', volumes[cryptocurrency] * lowest_price[cryptocurrency], cryptocurrency)
                    print('You have left:', amount, 'USD')
                else:
                    print('You can buy:', amount / lowest_price[cryptocurrency], cryptocurrency)
                    amount = 0
                    print('You have no money left:','USD')

        time.sleep(300)

maximal_profit(5000000)