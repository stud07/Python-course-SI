import requests as rq


def data_bitbay():
    response = rq.get('https://bitbay.net/API/Public/BTC/orderbook.json')
    return response.json()


def data_blockchain():
    response = rq.get('https://blockchain.info/ticker')
    return response.json()


data_bitbay = data_bitbay()
data_blockchain = data_blockchain()


print('[exchange rate in USD, amount of Bitcoin] \nBid offers for Bitcoin from Bitbay:')
for i in data_bitbay['bids']:
    print(i)


print('Ask offers for Bitcoin from Bitbay:')
for i in data_bitbay['asks']:
    print(i)


print('')
print('Bitcoin pricing from Blockchain: {}'.format(data_blockchain['USD']))


if data_bitbay['bids'][0][0] > data_blockchain['USD']['buy']:
    print('Buy Bitcoin from Bitbay.')
else:
    print('Buy Bitcoin from Blockchain.')



if data_bitbay['asks'][0][0] > data_blockchain['USD']['sell']:
    print('Sell Bitcoin at Bitbay.')
else:
    print('Sell Bitcoin at Blockchain.')
