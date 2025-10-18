"""Presentation layer primitives for btcwidget."""

from __future__ import annotations

from dataclasses import dataclass

from .application import PriceService
from .domain import PriceQuote


@dataclass(frozen=True, slots=True)
class WidgetSnapshot:
    """Immutable representation of the widget state."""

    title: str
    currency: str
    price: float


class BitcoinWidget:
    """Minimal presentation layer facade for the price widget."""

    def __init__(self, *, service: PriceService, title: str = "Bitcoin Widget") -> None:
        self._service = service
        self._title = title
        self._currency: str
        self._price: float
        self._initialise_state()

    def _initialise_state(self) -> None:
        quote = self._service.fetch_latest()
        self._currency = quote.currency
        self._price = quote.value

    def snapshot(self) -> WidgetSnapshot:
        """Return a snapshot of the widget state."""

        return WidgetSnapshot(title=self._title, currency=self._currency, price=self._price)

    def refresh(self) -> PriceQuote:
        """Update the widget state with the latest quote."""

        quote = self._service.fetch_latest()
        self._currency = quote.currency
        self._price = quote.value
        return quote
