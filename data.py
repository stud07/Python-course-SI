import requests as rq
import csv
import os

def price_data_USD():
    ETH = rq.get("https://bitbay.net/API/Public/ETHUSD/ticker.json")
    BTC = rq.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
    LTC = rq.get("https://bitbay.net/API/Public/LTCUSD/ticker.json")
    BCC = rq.get("https://bitbay.net/API/Public/BCCUSD/ticker.json")
    GAME = rq.get("https://bitbay.net/API/Public/GAMEUSD/ticker.json")
    EUR = rq.get("https://bitbay.net/API/Public/EURUSD/ticker.json")
    return ETH.json(), BTC.json(), LTC.json(), BCC.json(), GAME.json(), EUR.json()

def price_data_EUR():
    ETH = rq.get("https://bitbay.net/API/Public/ETHEUR/ticker.json")
    BTC = rq.get("https://bitbay.net/API/Public/BTCEUR/ticker.json")
    LTC = rq.get("https://bitbay.net/API/Public/LTCEUR/ticker.json")
    BCC = rq.get("https://bitbay.net/API/Public/BCCEUR/ticker.json")
    GAME = rq.get("https://bitbay.net/API/Public/GAMEEUR/ticker.json")
    return ETH.json(), BTC.json(), LTC.json(), BCC.json(), GAME.json()

def values_input():
    resources = {}
    ETH, BTC, LTC, BCC, GAME, EUR  = price_data_USD()
    cryptos_list = [ETH, BTC, LTC, BCC, GAME, EUR]
    currency_names= ['ETH', 'BTC', 'LTC', 'BCC', 'GAME', 'EUR']
    print('Choose resource from', (currency_names),'\n Press Q to quit')
    with open('resources.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        while True:
            name = input("Give the resource name: ").upper()
            if name == 'Q':
                return resources
            else:
                index = currency_names.index(name)
                if cryptos_list[index]['volume'] == 0:
                    print('No',name)
                    continue
                else:
                    quantity = float(input('Enter quantity'))
                    formula = round(((float(cryptos_list[index]['last']) - float(cryptos_list[index]['vwap'])) / float(cryptos_list[index]['last'])) * 100, 2)
                    resources[name] = quantity
                    csv_writer.writerow([name, quantity, formula])

def resource():
    print('Your resources are:\n','Name and quantity')
    with open('resources.csv', 'r') as read:
        reader = csv.reader(read)
        for row in reader:
            print(row[0], row[1])

def percentage():
    with open('resources.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        perecentage_sum = 0
        for row in csv_reader:
            if float(row[2]) > 0:
                print(row[0],'---->', float(row[2]))
            elif float(row[2]) == 0:
                print("0%")
            else:
                print(row[0], '----->', float(row[2]))
            perecentage_sum += float(row[2])
        print('Your profit:', (round(perecentage_sum, 1)))

def value_check_USD():
    ETH, BTC, LTC, BCC, GAME, EUR = price_data_USD()
    cryptos_list = [ETH, BTC, LTC, BCC, GAME, EUR]
    currency_names = ['ETH', 'BTC', 'LTC', 'BCC', 'GAME', 'EUR']
    with open('resources.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            name = row[0]
            index = list_of_names.index(name)
            price = float(cryptos_list[index]['vwap'])
            amount = float(row[1])
            print(name,'costs', price * amount, 'USD')

def value_check_EUR():
    ETH, BTC, LTC, BCC, GAME, EUR = price_data_USD()
    cryptos_list = [ETH, BTC, LTC, BCC, GAME, EUR]
    currency_names = ['ETH', 'BTC', 'LTC', 'BCC', 'GAME', 'EUR']
    with open('resources.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            name = row[0]
            if name == 'EUR':
                print('EUR is:',row[1])
            else:
                index = currency_names.index(name)
                price = float(cryptos_list[index]['vwap'])
                amount = float(row[1])
                print(name,'costs', price* amount, 'EUR')

def new_resource():
    resources = {}
    ETH, BTC, LTC, BCC, GAME, EUR = price_data_USD()
    cryptos_list = [ETH, BTC, LTC, BCC, GAME, EUR]
    currency_names = ['ETH', 'BTC', 'LTC', 'BCC', 'GAME', 'EUR']
    with open('resources.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            print(row[0], row[1])
    name = input('Enter the name of the resource \n')
    if name in currency_names:
        with open('resources.csv', 'a') as appendFile:
            writer = csv.writer(appendFile)
            index = currency_names.index(name)
            if cryptos_list[index]['volume'] == 0:
                print('No',name)
            else:
                quantity = float(input('Enter the quantity of the resource: '))
                formula = round(((float(cryptos_list[index]['last']) - float(cryptos_list[index]['vwap'])) / float(cryptos_list[index]['last'])) * 100, 2)
                resources[name] = quantity
                writer.writerow([name, quantity, formula])
    elif name == 'Q':
        print('Closed')
    else:
        print('Something went wrong')


def delete_resource():
    currency_names = ['ETH', 'BTC', 'LTC', 'BCC', 'GAME', 'EUR']
    lines = list()
    with open('resources.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            print(row[0])
    name = input('Choose resource to delete? \n')
    if name in currency_names:
        with open('resources.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for element in row:
                    if element == name:
                        lines.remove(row)
        with open('resources.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    elif name == 'Q':
        print('Closed')
    else:
        print('Something went wrong')


def change_the_quantity():
    currency_names = ['ETH', 'BTC', 'LTC', 'BCC', 'GAME', 'EUR']
    lines = list()
    with open('resources.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            print(row[0], row[1])
    name = input('Choose resource to change').upper()
    if name in currency_names:
        quantity = input('Give new quantity:')
        with open('resources.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for element in row:
                    if element == name:
                        row[1] = quantity
        with open('resources.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    elif name == 'Q':
        print('Closed')
    else:
        print('Something went wrong')


def clear():
    with open('resources.csv', 'w') as readFile:
        readFile.truncate()
    print('All resources deleted')


def check_condition():
    file_path = 'resources.csv'
    if os.stat(file_path).st_size == 0:
        print('Does not exist')