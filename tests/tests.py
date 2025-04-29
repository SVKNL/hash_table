import unittest

from hash_table import MyDict

class TestMyDict(unittest.TestCase):

    def setUp(self):
        self.my_dict = MyDict()

    def test_set_than_get_item(self):
        self.my_dict['test_key'] = 'test_value'
        self.assertEqual(self.my_dict['test_key'], 'test_value')

    def test_update_item(self):
        self.my_dict['test_key'] = 'test_value'
        self.my_dict['test_key'] = 'test_value2'
        self.assertEqual(self.my_dict['test_key'], 'test_value2')

    def test_delete_item(self):
        self.my_dict['test_key'] = 'test_value'
        del self.my_dict['test_key']
        with self.assertRaises(KeyError):
            self.my_dict['test_key']

    def test_contains_item(self):
        self.my_dict['test_key'] = 'test_value'
        self.assertTrue('test_key' in self.my_dict)

    def test_len(self):
        self.assertEqual(len(self.my_dict), 0)
        self.my_dict['test_key'] = 'test_value'
        self.assertEqual(len(self.my_dict), 1)
