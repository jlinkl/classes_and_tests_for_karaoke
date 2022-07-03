import unittest

from classes.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("Coke", 3)

    def test_drink(self):
        self.assertEqual("Coke", self.bar.drink)
    
    def test_price(self):
        self.assertEqual(3, self.bar.price)
