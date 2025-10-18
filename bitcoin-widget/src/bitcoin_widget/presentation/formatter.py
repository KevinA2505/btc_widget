"""Utility helpers for turning widget state into strings."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from ..domain import PriceQuote


@dataclass
class DisplayFormatter:
    """Build human readable widget output."""

    def render(self, quote: Optional[PriceQuote]) -> str:
        if quote is None:
            return "Bitcoin price is unavailable."
        timestamp = _format_timestamp(quote.timestamp)
        return f"Bitcoin Price: {quote.value:,.2f} {quote.currency} (source: {quote.source}, updated {timestamp})"


def _format_timestamp(value: datetime) -> str:
    return value.strftime("%Y-%m-%d %H:%M:%S %Z") or value.isoformat()
