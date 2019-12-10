import unittest
from app import ttd


class TestCase(unittest.TestCase):
    def test_ttd_return_Te(self):
        expect = 6
        value = ttd(expect)
        self.assertEqual(value, 'Te')

    def test_ttd_return_Ko(self):
        expect = 10
        value = ttd(expect)
        self.assertEqual(value, 'Ko')

    def test_ttd_return_Teko(self):
        expect = 15
        value = ttd(expect)
        self.assertEqual(value, 'Teko')

    def test_ttd_return_x(self):
        expect = 8
        value = ttd(expect)
        self.assertEqual(expect, value)
