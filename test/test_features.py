import unittest
from app import ttd, create_app_setting


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


class AppSettingTestCase(unittest.TestCase):
    def test_required_key_field(self):
        data = {
            'value': 'abc'
        }
        value = create_app_setting(data)
        self.assertEqual(value, "Required Fields")

    def test_required_value_field(self):
        data = {
            'key': 'abc'
        }
        value = create_app_setting(data)
        self.assertEqual(value, "Required Fields")

    def test_invalid_key_data(self):
        data = {
            'value': 'value',
            'key': 'type3'
        }
        value = create_app_setting(data)
        self.assertEqual(value, "Invalid Key")

    def test_invalid_value_data(self):
        data = {
            'value': True,
            'key': 'type1'
        }
        value = create_app_setting(data)
        self.assertEqual(value, 'Invalid Value')

    def test_create_success(self):
        data = {
            'value': 'value',
            'key': 'type1'
        }
        value = create_app_setting(data)
        self.assertEqual(data.get('value'), value.get('value'))
        self.assertEqual(data.get('key'), value.get('key'))
