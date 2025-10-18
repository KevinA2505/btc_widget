"""Public package interface for the bitcoin_widget project."""

from .presentation.widget import BitcoinWidget, WidgetState
from .application.price_service import PriceService
from .infrastructure.coingecko import CoinGeckoPriceProvider

__all__ = [
    "BitcoinWidget",
    "WidgetState",
    "PriceService",
    "CoinGeckoPriceProvider",
]
