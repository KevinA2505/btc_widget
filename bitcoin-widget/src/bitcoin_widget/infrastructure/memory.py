"""In-memory utilities useful for testing and local development."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator, Optional

from ..domain import PriceProvider, PriceQuote


@dataclass
class InMemoryPriceProvider(PriceProvider):
    """Price provider backed by pre-computed quotes."""

    quotes: Iterable[PriceQuote]

    def __post_init__(self) -> None:
        self._iterator: Iterator[PriceQuote] = iter(self.quotes)
        self._last: Optional[PriceQuote] = None

    def fetch_price(self, currency: str = "USD") -> PriceQuote:
        try:
            self._last = next(self._iterator)
        except StopIteration as exc:  # pragma: no cover - defensive guard
            raise RuntimeError("No quotes left in provider") from exc
        if self._last.currency != currency.upper():
            raise ValueError(f"Quote currency {self._last.currency} does not match requested {currency}")
        return self._last

    @property
    def last(self) -> Optional[PriceQuote]:
        """Return the last served quote."""

        return self._last
