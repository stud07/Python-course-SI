import requests as rq

def data_bitbay():
    response = rq.get('https://bitbay.net/API/Public/BTC/ticker.json')
    return response.json()

def data_blockchain():
    response = rq.get('https://blockchain.info/ticker')
    return response.json()

def data_bitstamp():
    response = rq.get('https://www.bitstamp.net/api/ticker')
    return response.json()

def data_cex():
    response = rq.get('https://cex.io/api/ticker/BTC/USD')
    return response.json()



def Arbritrage(wallet):
    bitbay = data_bitbay()
    blockchain = data_blockchain()
    bitstamp = data_bitstamp()
    cex = data_cex()

    bitbay_bid = float(bitbay['bid'])
    bitbay_ask = float(bitbay['ask'])

    blockchain_bid = float(blockchain['USD']['buy'])
    blockchain_ask = float(blockchain['USD']['sell'])

    bitstamp_bid = float(bitstamp['bid'])
    bitstamp_ask = float(bitstamp['ask'])

    cex_bid = float(cex['bid'])
    cex_ask = float(cex['ask'])

    sell = {'bitbay':bitbay_bid,'blockchain':blockchain_bid,'bitstamp':bitstamp_bid}
    buy = {'bitbay':bitbay_ask,'blockchain':blockchain_ask,'bitstamp':bitstamp_ask}

    best_to_buy = min(buy.values())
    best_to_sell = max(sell.values())


    Taker = [0.0043, 0.024, 0.005]

    buy = [bitbay_ask, blockchain_ask, bitstamp_ask,cex_ask]
    sell = [bitbay_bid, blockchain_bid, bitstamp_bid,cex_bid]

    usd = wallet[0]
    btc = wallet[1]


    for i in range(len(Taker)):
        buy[i] = ((Taker[i]+1)*buy[i]*btc)
        sell[i] = ((1-Taker[i])*sell[i]*btc)

    buy = max(buy)
    sell = min(sell)

    if sell > buy:
        income = sell - buy
        print('Buy',btc,'bitcoin',best_to_buy,'and sell',best_to_sell,'profit:',income)
        wallet[0] = sell
        wallet[1] = 0
        buy_ = wallet[0]/ best_to_buy
        wallet[0] = 0
        wallet[1] = buy_
        print('wallet:',wallet)
    else:
        print("Don't buy.")

wallet = [1,2]
Arbritrage(wallet)