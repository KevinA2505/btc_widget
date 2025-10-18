# BTC Widget

Mini proyecto de ejemplo que ilustra cómo estructurar un paquete Python con layout `src/` para mostrar el precio del Bitcoin.

## Estructura

```
btc_widget/
├── src/
│   └── btcwidget/
│       ├── __init__.py
│       ├── application.py
│       ├── domain.py
│       ├── infrastructure.py
│       └── presentation.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_widget.py
└── pyproject.toml
```

## Cómo ejecutar pruebas

1. Crear y activar un entorno virtual (por ejemplo `.venv`).
2. Ejecutar los siguientes comandos para preparar el proyecto:

```bash
python -m pip install -U pip
pip install -e .
pip install -r requirements-dev.txt
```

3. Lanzar la suite de pruebas:

```bash
pytest
```
