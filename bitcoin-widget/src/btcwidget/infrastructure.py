"""Infrastructure utilities for btcwidget."""

from __future__ import annotations

from collections.abc import Iterable
from typing import List, Protocol

from .domain import PriceQuote


class PriceProvider(Protocol):
    """Protocol representing a source of ``PriceQuote`` instances."""

    def latest(self, *, currency: str | None = None) -> PriceQuote:
        """Return the most recent quote available for the requested currency."""


class InMemoryPriceProvider:
    """Simple provider that serves pre-defined ``PriceQuote`` instances."""

    def __init__(self, *, quotes: Iterable[PriceQuote]) -> None:
        self._quotes: List[PriceQuote] = list(quotes)

    def latest(self, *, currency: str | None = None) -> PriceQuote:
        """Return the most recent quote available."""

        if not self._quotes:
            raise LookupError("No price quotes are available.")

        if currency is None:
            return self._quotes[0]

        currency_code = currency.upper()
        for quote in self._quotes:
            if quote.currency == currency_code:
                return quote
        raise ValueError(f"No quotes available for currency '{currency_code}'.")
