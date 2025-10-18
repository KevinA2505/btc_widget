from btcwidget.application import PriceService
from btcwidget.domain import PriceQuote
from btcwidget.infrastructure import InMemoryPriceProvider
from btcwidget.presentation import BitcoinWidget


def test_widget_initial_state() -> None:
    quote = PriceQuote.from_raw(value=42_000.0, currency="USD", source="test")
    provider = InMemoryPriceProvider(quotes=[quote])
    service = PriceService(provider=provider)
    widget = BitcoinWidget(service=service)

    snapshot = widget.snapshot()

    assert snapshot.title == "Bitcoin Widget"
    assert snapshot.currency == "USD"
    assert snapshot.price == 42_000.0
