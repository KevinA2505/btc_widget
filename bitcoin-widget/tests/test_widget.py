import unittest
from bitcoin_widget.widget import BitcoinWidget

class TestBitcoinWidget(unittest.TestCase):

    def setUp(self):
        self.widget = BitcoinWidget()

    def test_initialization(self):
        self.assertIsNotNone(self.widget)
        self.assertEqual(self.widget.title, "Bitcoin Widget")
        self.assertEqual(self.widget.price, 0)

    def test_update_price(self):
        self.widget.update_price(50000)
        self.assertEqual(self.widget.price, 50000)

    def test_display(self):
        self.widget.update_price(60000)
        display_output = self.widget.display()
        self.assertIn("Bitcoin Price:", display_output)
        self.assertIn("60000", display_output)

if __name__ == '__main__':
    unittest.main()