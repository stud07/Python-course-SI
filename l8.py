import requests
import time
import matplotlib.pyplot as plt
import pandas as pd

def get_data(crypto):
    now_from = 1588291200
    now = time.time()
    past = 1559260800
    past_from = past - (now - now_from)
    past_crypto = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=BTC_{}&start={}&end={}&period=14400".format(crypto, past_from, past))
    now_crypto = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=BTC_{}&start={}&end={}&period=14400".format(crypto, now_from, now))
    return past_crypto.json(), now_crypto.json()

def time_(time):
    volumes = []
    for item in time:
        volumes.append(item['volume'])
    return volumes

def avg(data):
    size = 15
    numbers_series = pd.Series(data)
    windows = numbers_series.rolling(size)
    moving_averages = windows.mean()
    moving_averages_list = moving_averages.tolist()
    without_nans = moving_averages_list[size - 1:]
    return without_nans

def simulation(volume):
    size = 100
    simulated = []

    for i in range(size):
        simulation_data = avg(volume)
        simulated.append(simulation_data)
    result = []
    for i in range(len(simulated[0])):
        values = []
        for j in range(len(simulated)):
            values.append(simulated[j][i])
        average = sum(values) / len(values)
        result.append(average)
    return result


def plots(vol, one, avg, title):
    plt.figure(figsize=(18, 8))
    plt.subplot(2, 2, 1)
    plt.plot(vol, '-r')
    plt.title("Volume")
    plt.subplot(2, 2, 2)
    plt.plot(one, '-g')
    plt.title("One simulation")
    plt.subplot(2, 2, 3)
    plt.plot(avg, '-b')
    plt.title("Avg simulation")
    plt.suptitle(title, fontsize=18)
    plt.show()


name = input("Choose your cryptocurrency (ETC, DASH, LTC): ")
print("month-->this year--->last year")
past, present = get_data(name)
past_volume = time_(past)
present_volume = time_(present)
one_simulation_past = avg(past_volume)
one_simulation_present = avg(present_volume)
avg_simulation_past = simulation(past_volume)
avg_simulation_present = simulation(present_volume)
plots(past_volume, one_simulation_past, avg_simulation_past, "last year")
plots(present_volume, one_simulation_present, avg_simulation_present, "this year")
