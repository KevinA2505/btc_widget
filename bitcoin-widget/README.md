# Bitcoin Widget Application

This project is a Bitcoin widget application that allows users to view real-time Bitcoin data and interact with it through a user-friendly interface.

## Project Structure

```
bitcoin-widget
├── src
│   └── bitcoin_widget
│       ├── __init__.py
│       ├── main.py
│       ├── widget.py
│       ├── api.py
│       ├── ui.py
│       └── utils.py
├── tests
│   ├── __init__.py
│   └── test_widget.py
├── pyproject.toml
├── requirements.txt
├── setup.cfg
├── .gitignore
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd bitcoin-widget
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python -m src.bitcoin_widget.main
```

## Testing

To run the tests, use the following command:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.