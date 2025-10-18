"""Configuration helpers for the bitcoin_widget package."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta


def _default_poll_interval() -> timedelta:
    """Return a sensible default polling interval for price updates."""

    return timedelta(minutes=1)


@dataclass(frozen=True)
class Settings:
    """Application level configuration."""

    currency: str = "USD"
    poll_interval: timedelta = _default_poll_interval()
    data_source: str = "CoinGecko"


DEFAULT_SETTINGS = Settings()
"""Default configuration used by the CLI entry point and tests."""
