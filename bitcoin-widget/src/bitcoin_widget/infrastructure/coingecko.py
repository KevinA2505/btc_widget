"""Adapter for retrieving prices from the public CoinGecko API."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Final
from urllib import request, parse

from ..domain import PriceProvider, PriceQuote


@dataclass
class CoinGeckoPriceProvider(PriceProvider):
    """Retrieve bitcoin prices using the public CoinGecko REST API."""

    source: Final[str] = "CoinGecko"
    base_url: Final[str] = "https://api.coingecko.com/api/v3/simple/price"
    timeout: float = 8.0

    def fetch_price(self, currency: str = "USD") -> PriceQuote:
        params = {"ids": "bitcoin", "vs_currencies": currency.lower()}
        url = f"{self.base_url}?{parse.urlencode(params)}"
        with request.urlopen(url, timeout=self.timeout) as response:
            payload = json.load(response)
        value = float(payload["bitcoin"][currency.lower()])
        return PriceQuote.from_raw(value=value, currency=currency, source=self.source)
