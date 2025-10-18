import urllib.request
import urllib.parse
import json
from typing import Dict, Any

class PriceProvider:
    def get_btc_price(self, currency: str = "usd") -> float:
        raise NotImplementedError

class CoinGeckoProvider(PriceProvider):
    BASE = "https://api.coingecko.com/api/v3/simple/price"

    def get_btc_price(self, currency: str = "usd") -> float:
        params: Dict[str, Any] = {"ids": "bitcoin", "vs_currencies": currency}
        url = f"{self.BASE}?{urllib.parse.urlencode(params)}"
        with urllib.request.urlopen(url, timeout=8) as resp:
            # urllib raises HTTPError for non-2xx responses, so direct read is fine
            data = json.load(resp)
        return float(data["bitcoin"][currency])

def default_provider() -> PriceProvider:
    return CoinGeckoProvider()
