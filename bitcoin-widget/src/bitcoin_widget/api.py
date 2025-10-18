def fetch_bitcoin_price():
    import requests

    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['bpi']['USD']['rate_float']
    else:
        raise Exception("Error fetching Bitcoin price")

def fetch_historical_data(start_date, end_date):
    import requests

    url = f"https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['bpi']
    else:
        raise Exception("Error fetching historical Bitcoin data")