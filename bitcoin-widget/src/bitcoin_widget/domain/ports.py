"""Abstractions that infrastructure adapters must implement."""

from __future__ import annotations

from abc import ABC, abstractmethod

from .models import PriceQuote


class PriceProvider(ABC):
    """Protocol describing how to retrieve bitcoin prices."""

    @abstractmethod
    def fetch_price(self, currency: str = "USD") -> PriceQuote:
        """Return the current bitcoin price in ``currency``."""

        raise NotImplementedError
