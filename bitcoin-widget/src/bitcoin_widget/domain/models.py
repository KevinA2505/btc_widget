"""Domain entities used by the bitcoin_widget package."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class PriceQuote:
    """Represents a bitcoin price returned by an upstream provider."""

    value: float
    currency: str
    source: str
    timestamp: datetime

    def __post_init__(self) -> None:
        """Normalise invariant fields after initialisation."""

        object.__setattr__(self, "currency", self.currency.upper())

    @classmethod
    def from_raw(cls, value: float, currency: str, source: str) -> "PriceQuote":
        """Create a :class:`PriceQuote` from raw provider values."""

        return cls(value=value, currency=currency.upper(), source=source, timestamp=datetime.now(timezone.utc))
