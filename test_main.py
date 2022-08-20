import unittest
from unittest import TestCase
from main import name_as_uppercase


class Test(TestCase):
    def test_name_as_uppercase(self):
        new_name = name_as_uppercase('ahmet')
        self.assertEqual('ahmet'.upper(), new_name)


if __name__ == '__main__':
    unittest.main()
