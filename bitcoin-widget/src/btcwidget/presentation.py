"""Presentation layer primitives for btcwidget."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

from .application import PriceService
from .domain import PriceQuote


@dataclass(frozen=True, slots=True)
class WidgetSnapshot:
    """Immutable representation of the widget state."""

    title: str
    currency: str
    price: float | None
    last_quote: PriceQuote | None
    history: Sequence[PriceQuote]


class BitcoinWidget:
    """Minimal presentation layer facade for the price widget."""

    def __init__(
        self,
        *,
        service: PriceService,
        title: str = "Bitcoin Widget",
        currency: str = "USD",
    ) -> None:
        self._service = service
        self._title = title
        self._currency = currency.upper()
        self._price: float | None = None
        self._last_quote: PriceQuote | None = None
        self._history: List[PriceQuote] = []

    @property
    def price(self) -> float | None:
        return self._price

    def snapshot(self) -> WidgetSnapshot:
        """Return a snapshot of the widget state."""

        return WidgetSnapshot(
            title=self._title,
            currency=self._currency,
            price=self._price,
            last_quote=self._last_quote,
            history=list(self._history),
        )

    def fetch_price(self) -> PriceQuote:
        """Update the widget state with the latest quote."""

        quote = self._service.fetch_latest(currency=self._currency)
        self._register_quote(quote)
        return quote

    def update_price(self, value: float, *, source: str = "manual") -> PriceQuote:
        quote = PriceQuote.from_raw(value=value, currency=self._currency, source=source)
        self._register_quote(quote)
        return quote

    def display(self) -> str:
        if self._price is None:
            return f"{self._title}: price unavailable"
        return f"{self._title}: Bitcoin Price {self._price:.2f} {self._currency}"

    def _register_quote(self, quote: PriceQuote) -> None:
        self._last_quote = quote
        self._price = quote.value
        self._history.append(quote)
