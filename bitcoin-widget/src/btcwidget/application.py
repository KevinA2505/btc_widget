"""Application services for btcwidget."""

from __future__ import annotations

from .domain import PriceQuote
from .infrastructure import InMemoryPriceProvider


class PriceService:
    """Provide access to Bitcoin price information."""

    def __init__(self, *, provider: InMemoryPriceProvider) -> None:
        self._provider = provider

    def fetch_latest(self) -> PriceQuote:
        """Fetch the latest available price quote."""

        return self._provider.latest()
