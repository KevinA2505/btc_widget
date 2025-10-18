def format_btc_amount(amount):
    """Format the Bitcoin amount to a string with 8 decimal places."""
    return f"{amount:.8f} BTC"

def is_valid_btc_address(address):
    """Check if the provided Bitcoin address is valid."""
    # A simple check for Bitcoin address length and prefix
    if len(address) in [26, 34] and (address.startswith('1') or address.startswith('3')):
        return True
    return False

def calculate_btc_value(amount, price_per_btc):
    """Calculate the value of a given amount of Bitcoin in USD."""
    return amount * price_per_btc

def fetch_current_btc_price(api_client):
    """Fetch the current Bitcoin price from an external API."""
    response = api_client.get('/v1/bpi/currentprice/BTC.json')
    if response.status_code == 200:
        return response.json()['bpi']['USD']['rate_float']
    return None