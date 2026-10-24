import unittest

from pricing import discounted_price


class DiscountedPriceTests(unittest.TestCase):
    def test_applies_discount_to_price(self):
        self.assertEqual(discounted_price(10000, 10), 9000)
