# Bitcoin Widget Application

A modular Python project that exposes a small API for retrieving and displaying Bitcoin price information. The codebase is organised using a lightweight layered architecture so that the presentation layer can remain independent from the external price providers.

## Project layout

```
bitcoin-widget/
├── src/
│   └── bitcoin_widget/
│       ├── __init__.py
│       ├── application/
│       │   └── price_service.py
│       ├── config.py
│       ├── domain/
│       │   ├── models.py
│       │   └── ports.py
│       ├── infrastructure/
│       │   ├── coingecko.py
│       │   └── memory.py
│       ├── main.py
│       └── presentation/
│           ├── formatter.py
│           └── widget.py
├── tests/
│   └── test_widget.py
├── pyproject.toml
├── requirements.txt
├── setup.cfg
└── README.md
```

## Getting started

Install the dependencies into a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the CLI demo

The project exposes a small command line script that fetches the current Bitcoin price using the public CoinGecko API.

```bash
python -m bitcoin_widget.main
```

## Running the tests

```bash
pytest
```

## Configuration

Configuration defaults live in `bitcoin_widget/config.py`. These settings can be customised by composing your own `PriceService` and `BitcoinWidget` instances.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
