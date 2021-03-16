import unittest
from src.utils import Security


class StringHelperTestCase(unittest.TestCase):

    def test_hashed_password(self):
        password = 'test1'
        wrong_password = b'test2'

        hashed_password = Security.get_hashed_password(password)
        self.assertTrue(Security.check_password(password, hashed_password))
        self.assertFalse(Security.check_password(password, wrong_password))
