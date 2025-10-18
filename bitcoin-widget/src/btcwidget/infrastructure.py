"""Infrastructure utilities for btcwidget."""

from __future__ import annotations

from collections.abc import Iterable
from typing import List

from .domain import PriceQuote


class InMemoryPriceProvider:
    """Simple provider that serves pre-defined ``PriceQuote`` instances."""

    def __init__(self, *, quotes: Iterable[PriceQuote]) -> None:
        self._quotes: List[PriceQuote] = list(quotes)

    def latest(self) -> PriceQuote:
        """Return the most recent quote available."""

        if not self._quotes:
            raise LookupError("No price quotes are available.")
        return self._quotes[0]
