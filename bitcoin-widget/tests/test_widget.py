from datetime import datetime, timezone

import pytest

from bitcoin_widget.application import PriceService
from bitcoin_widget.domain import PriceQuote
from bitcoin_widget.infrastructure import InMemoryPriceProvider
from bitcoin_widget.presentation import BitcoinWidget


@pytest.fixture
def price_service() -> PriceService:
    quote = PriceQuote.from_raw(value=42_000.0, currency="USD", source="test")
    provider = InMemoryPriceProvider(quotes=[quote])
    return PriceService(providers=[provider])


def test_widget_initial_state(price_service: PriceService) -> None:
    widget = BitcoinWidget(service=price_service)
    snapshot = widget.snapshot()

    assert snapshot.title == "Bitcoin Widget"
    assert snapshot.currency == "USD"
    assert snapshot.last_quote is None
    assert snapshot.history == []
    assert widget.price is None


def test_fetch_price_updates_state(price_service: PriceService) -> None:
    widget = BitcoinWidget(service=price_service)
    quote = widget.fetch_price()

    assert widget.price == pytest.approx(42_000.0)
    assert "Bitcoin Price" in widget.display()
    assert quote == widget.snapshot().last_quote


def test_manual_update_creates_quote(price_service: PriceService) -> None:
    widget = BitcoinWidget(service=price_service)
    manual_quote = widget.update_price(43_500.5)

    assert manual_quote.value == pytest.approx(43_500.5)
    assert manual_quote.source == "manual"
    assert manual_quote.currency == "USD"
    assert widget.price == pytest.approx(43_500.5)


def test_snapshot_returns_copy(price_service: PriceService) -> None:
    widget = BitcoinWidget(service=price_service)
    widget.update_price(41_000.0)

    snapshot = widget.snapshot()
    snapshot.history.append(PriceQuote.from_raw(0, "USD", "mutation"))

    assert len(widget.snapshot().history) == 1


def test_in_memory_provider_requires_matching_currency() -> None:
    quote = PriceQuote(value=40_000.0, currency="USD", source="test", timestamp=datetime.now(timezone.utc))
    provider = InMemoryPriceProvider(quotes=[quote])
    service = PriceService(providers=[provider])
    widget = BitcoinWidget(service=service, currency="EUR")

    with pytest.raises(ValueError):
        widget.fetch_price()


def test_price_quote_normalises_currency() -> None:
    quote = PriceQuote(value=39_500.0, currency="gbp", source="test", timestamp=datetime.now(timezone.utc))
    provider = InMemoryPriceProvider(quotes=[quote])
    widget = BitcoinWidget(service=PriceService(providers=[provider]), currency="GBP")

    fetched_quote = widget.fetch_price()

    assert fetched_quote.currency == "GBP"
