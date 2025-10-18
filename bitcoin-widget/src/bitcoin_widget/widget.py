class BitcoinWidget:
    def __init__(self):
        self.price = 0.0
        self.currency = "USD"

    def fetch_price(self):
        # Logic to fetch the current Bitcoin price from an API
        pass

    def display(self):
        # Logic to display the widget with the current price
        pass

    def update(self):
        self.fetch_price()
        self.display()