"""Simple command line interface for the Bitcoin widget."""

from __future__ import annotations

from .application import PriceService
from .config import DEFAULT_SETTINGS
from .infrastructure import CoinGeckoPriceProvider
from .presentation import BitcoinWidget


def build_widget() -> BitcoinWidget:
    provider = CoinGeckoPriceProvider()
    service = PriceService(providers=[provider])
    return BitcoinWidget(service=service, currency=DEFAULT_SETTINGS.currency)


def main() -> None:
    widget = build_widget()
    quote = widget.fetch_price()
    print(widget.display())
    print(f"Last updated at: {quote.timestamp.isoformat()}")


if __name__ == "__main__":
    main()
