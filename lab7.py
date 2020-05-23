import requests as rq
from scipy.stats import norm
import matplotlib.pyplot as plt
from random import *
from statistics import median
import numpy as np
import time

def get_data(timer, currency):
    vol = []
    difference = []
    predictlist = []
    url = "https://www.bitstamp.net/api/v2/ohlc/btcusd?step=86400&limit=10&start={timer}"
    print(url)
    dailyData = rq.get(url).json()['data']['ohlc']


def get_Data(date, currency):
    url = "https://www.bitstamp.net/api/v2/ohlc/{currency}usd?step=86400&limit=100&start={timer}"
    return rq.get(url).json()['data']['ohlc']

    for day in dailyData:
        vol.append([float(day['volume']), time.ctime(float(day['timestamp']))])

    for i in range(0, len(vol)):
        difference.append((vol[i][0]-vol[i-1][0])/vol[i][0])
def info(dailyData):
    for i in range(0, len(dailyData) - 1):
        vol.append(float(dailyData[i]['volume']))
        difference.append(absolute((vol[i] - vol[i - 1]) / vol[i]))
    return difference, vol

    print(difference)

def absolute(num):
    if num > 1:
        return num - 1
    elif num < -1:
        return num + 1
    else:
        return num


def simulation(data, vol):
    avg, std = norm.fit(data)
    predict = absolute(gauss(avg, std))
    predictList.append(predict * vol[-1] + vol[-1])
    plt.plot(arange(0, len(vol)), vol, color='r')
    plt.plot(arange(len(vol), len(predictList) + len(vol)), predictList, color='m')
    plt.xlabel("Days")
    plt.ylabel("Volume")
    plt.title("Prediction of volume")
    plt.legend(['Historical data','Predicted data'])


def pointer(predictList):
    med = median(predictList)
    avg, std = norm.fit(predictList)
    print('One simulation: ', predictList[0])
    print('Madian: ', med, '\nAvarange: ', avg, '\nStd: ', std)

timer = int(time.time())-86400*20

get_Data(str(timer), 'BTC')
def calculate(daysAnalyst, currency):
    difference, vol = information(get_Data(daysAnalyst, currency))
    for i in range(daysAnalyst):
        simulation(difference, vol)
    pointer(predictList)
    plt.show()
