import csv
import os
import time

import requests

DATA_URL = "http://api.nbp.pl/api/exchangerates/tables/C?format=json"
DATA_FILE_PATH = "currency.csv"
DATA_TIME_IN_SECONDS = 10 * 60


def save_data():
    response = requests.get(DATA_URL)
    data = response.json()
    currency_list = data[0]['rates']
    with open(DATA_FILE_PATH, 'w', newline='', encoding='UTF-8') as csvfile:
        fieldnames = ['currency', 'code', 'bid', 'ask']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for dana in currency_list:
            writer.writerow(
                {'currency': str(dana['currency']),
                 'code': str(dana['code']),
                 'bid': float(dana['bid']),
                 'ask': float(dana['ask'])}
            )
        csvfile.close()


def load_data():
    code = []
    bid = []
    ask = []
    with open(DATA_FILE_PATH, 'r', newline='', encoding='UTF-8') as csvfileload:
        read = csv.DictReader(csvfileload, delimiter=';')
        for row in read:
            code.append(row['code'])
            ask.append(row['ask'])
            bid.append(row['bid'])
    csvfileload.close()
    return code, bid, ask


def get_data():
    invalidation_time = (time.time() - DATA_TIME_IN_SECONDS)
    data = getattr(get_data, "data", None)
    data_read_time = getattr(get_data, "data_read_time", 0)
    if not data or data_read_time < invalidation_time:
        if not os.path.isfile(DATA_FILE_PATH) or os.stat(DATA_FILE_PATH).st_mtime < invalidation_time:
            save_data()
        data = load_data()
        get_data.data = data
        get_data.data_read_time = time.time()
    return get_data.data
