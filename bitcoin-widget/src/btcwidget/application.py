"""Application services for btcwidget."""

from __future__ import annotations

from .domain import PriceQuote
from collections.abc import Iterable

from .infrastructure import PriceProvider


class PriceService:
    """Provide access to Bitcoin price information."""

    def __init__(
        self,
        *,
        providers: Iterable[PriceProvider] | None = None,
        provider: PriceProvider | None = None,
    ) -> None:
        if providers is not None and provider is not None:
            raise ValueError("Pass either 'providers' or 'provider', not both.")

        if providers is None:
            providers = [provider] if provider is not None else []

        self._providers = list(providers)
        if not self._providers:
            raise ValueError("At least one price provider must be configured.")

    def fetch_latest(self, *, currency: str | None = None) -> PriceQuote:
        """Fetch the latest available price quote."""

        currency_code = currency.upper() if currency else None
        last_error: Exception | None = None
        for provider in self._providers:
            try:
                quote = provider.latest(currency=currency_code)
            except LookupError as error:
                last_error = error
                continue
            except ValueError:
                # Currency mismatch for this provider; try the next one.
                continue
            if currency_code is None or quote.currency == currency_code:
                return quote

        if currency_code is not None:
            raise ValueError(f"No price quote available for currency '{currency_code}'.")
        if last_error is not None:
            raise last_error
        raise LookupError("No price quotes are available from any provider.")
