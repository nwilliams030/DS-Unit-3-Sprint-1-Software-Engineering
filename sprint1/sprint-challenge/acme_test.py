"""
Part 5 of Unit 3 sprint challenge.

Unit testing our code.
"""
#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, generate_report, ADJECTIVES, NOUNS


class AcmeProdTest(unittest.TestCase):
    """
    Making sure Acme products are the tops!
    """
    def test_default_price_self(self):
        """
        Test default price == 10
        """
        prod = Product('Test Product 1')
        self.assertEqual(prod.price, 10)

    def test_default_weight_self(self):
        """
        Test default weight == 20
        """
        prod = Product('Test Product 2')
        self.assertEqual(prod.weight, 20)

    def test_explode_method(self):
        """
        Ensure explode works
        """
        prod = Product('Test Product Bomb')
        self.assertIsNotNone(prod.explode)

    def test_steal_method(self):
        """
        Ensure stealability working
        """
        prod = Product('Test Product Stolen')
        self.assertIsNotNone(prod.stealability)


class AcmeReportTest(unittest.TestCase):
    """
    Verify reporter working as intended
    """
    def test_default_num_products(self):
        """
        Assert number of generated products!
        """
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """
        Confirm names are all properly assembled.
        """
        products = generate_products()
        for x in products:
            self.assertIn(x.name.split()[0], ADJECTIVES)
            self.assertIn(x.name.split()[1], NOUNS)

    def test_report_names(self):
        """
        Confirm names are randomly generated.
        """
        report = generate_report(generate_products())
        self.assertGreaterEqual(len(set(report[0])), 2)

    def test_report_price_range(self):
        """
        Confirm price range acceptable limits.
        """
        report = generate_report(generate_products())
        self.assertGreaterEqual(min(report[1]), 5.00)
        self.assertLessEqual(max(report[1]), 1938.67)


if __name__ == "__main__":
    unittest.main()
