"""Application service for retrieving bitcoin prices."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional

from ..domain import PriceProvider, PriceQuote


@dataclass
class PriceService:
    """Facade around one or more :class:`PriceProvider` implementations."""

    providers: Iterable[PriceProvider]

    def __post_init__(self) -> None:
        self._providers = tuple(self.providers)
        if not self._providers:
            raise ValueError("At least one PriceProvider must be supplied")

    def fetch_latest(self, currency: str = "USD") -> PriceQuote:
        """Return the first successful price quote from the configured providers."""

        last_error: Optional[Exception] = None
        for provider in self._providers:
            try:
                quote = provider.fetch_price(currency)
            except Exception as error:  # pragma: no cover - defensive logging hook
                last_error = error
                continue
            else:
                return quote
        if last_error is None:
            raise RuntimeError("No providers configured")
        # Bubble up the last provider error to make debugging easier for callers.
        raise last_error
