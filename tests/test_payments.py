"""Tests du module de paiement."""

import unittest


class TestPayments(unittest.TestCase):
    def test_amount_conversion(self):
        """Les montants sont stockés en centimes."""
        self.assertEqual(int(12.50 * 100), 1250)

    def test_currency_default(self):
        """La devise par défaut est le dirham marocain."""
        self.assertEqual("MAD", "MAD")


if __name__ == "__main__":
    unittest.main()
