import requests
import pandas as pd

symbol = "IBM&apikey=demo"
api_key = 'BH26ADJ3QCPFGST3'
time_series_weekly = 'TIME_SERIES_WEEKLY'
time_series_monthly = 'TIME_SERIES_MONTHLY'
time_series_daily= 'TIME_SERIES_DAILY'

time_search_daily = 'Time Series (Daily)'
time_search_monthly = 'Monthly Time Series'
time_search_weekly = 'Weekly Time Series'


def konacna_funckija(periodicnost):
    if periodicnost == 'daily':
        frekvencija = time_series_daily
    elif periodicnost == 'weekly':
        frekvencija = time_series_weekly
    elif periodicnost == 'monthly':
        frekvencija =  time_series_monthly
    else:
        print('Nothing to search')

    if periodicnost == 'weekly':
        pretrazivanje =  time_search_weekly
    elif periodicnost == 'daily':
        pretrazivanje = time_search_daily
    elif periodicnost == 'monthly':
        pretrazivanje = time_search_monthly
    else:
        print('Nothing to search')

    api_base_url = 'https://www.alphavantage.co'
    endpoint_path = f"{api_base_url}/query?function={frekvencija}&symbol={symbol}"
    r = requests.get(endpoint_path)
    if r.status_code in range(200, 299):
        data = r.json()
        times = data[f'{pretrazivanje}']
        index1 = times.keys()
        values = times.values()
        kolone = ['open', 'high', 'low', 'close', 'volume']
        podaci = []
        for value in values:
            open, high, low, close, volume = (value.values())
            _ = [open, high, low, close, volume]
            podaci.append(_)
        df = pd.DataFrame(podaci, columns=kolone, index=index1)
        df.to_csv(f'{periodicnost}.csv')

print(konacna_funckija(''))




# df.to_csv(output)