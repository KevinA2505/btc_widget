from pathlib import Path

APP_NAME = "CryptoWidget"
CURRENCY = "usd"
REFRESH_MS = 15_000  # 15s (luego podrás hacer esto configurable)
HISTORY_POINTS = 120  # ~30 min si refrescas cada 15s

# Estilos
THEME_QSS = (Path(__file__).parent / "ui" / "styles.qss").as_posix()

# Iconos (opcionales por ahora)
ICON_ICO = Path(__file__).parents[2] / "assets" / "icon.ico"
ICON_PNG = Path(__file__).parents[2] / "assets" / "icon.png"
