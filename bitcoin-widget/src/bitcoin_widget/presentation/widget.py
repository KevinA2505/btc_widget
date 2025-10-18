"""High level widget abstraction that coordinates services and rendering."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from ..application import PriceService
from ..domain import PriceQuote
from .formatter import DisplayFormatter


@dataclass
class WidgetState:
    """Immutable snapshot of the widget state."""

    title: str
    currency: str
    last_quote: Optional[PriceQuote]
    history: List[PriceQuote]


@dataclass
class BitcoinWidget:
    """User facing component that exposes a simple API for consumers."""

    service: PriceService
    title: str = "Bitcoin Widget"
    currency: str = "USD"
    formatter: DisplayFormatter = field(default_factory=DisplayFormatter)

    _history: List[PriceQuote] = field(default_factory=list, init=False)
    _last_quote: Optional[PriceQuote] = field(default=None, init=False)
    _last_refresh: Optional[datetime] = field(default=None, init=False)

    def fetch_price(self) -> PriceQuote:
        """Retrieve a fresh price quote using the configured service."""

        quote = self.service.fetch_latest(self.currency)
        self._last_quote = quote
        self._history.append(quote)
        self._last_refresh = quote.timestamp
        return quote

    def update_price(self, value: float) -> PriceQuote:
        """Manually update the widget with an externally provided price."""

        quote = PriceQuote.from_raw(value=value, currency=self.currency, source="manual")
        self._last_quote = quote
        self._history.append(quote)
        self._last_refresh = quote.timestamp
        return quote

    @property
    def price(self) -> Optional[float]:
        return None if self._last_quote is None else self._last_quote.value

    def display(self) -> str:
        """Return a textual representation of the widget state."""

        return self.formatter.render(self._last_quote)

    def snapshot(self) -> WidgetState:
        """Return an immutable representation of the widget state."""

        return WidgetState(
            title=self.title,
            currency=self.currency,
            last_quote=self._last_quote,
            history=list(self._history),
        )

    @property
    def last_updated(self) -> Optional[datetime]:
        """Return when the widget was last refreshed."""

        return self._last_refresh
