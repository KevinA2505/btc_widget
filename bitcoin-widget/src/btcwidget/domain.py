"""Domain models for btcwidget."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class PriceQuote:
    """Represents a single Bitcoin price quote."""

    value: float
    currency: str
    source: str
    timestamp: datetime

    @classmethod
    def from_raw(
        cls,
        *,
        value: float,
        currency: str,
        source: str,
        timestamp: datetime | None = None,
    ) -> "PriceQuote":
        """Create a ``PriceQuote`` normalising the currency code."""

        normalised_currency = currency.upper()
        quote_timestamp = timestamp or datetime.now(timezone.utc)
        return cls(
            value=float(value),
            currency=normalised_currency,
            source=source,
            timestamp=quote_timestamp,
        )
