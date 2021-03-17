import unittest
from src.utils import Security


class StringHelperTestCase(unittest.TestCase):

    def test_hashed_password(self):
        password = 'test1'
        wrong_password = 'test123'
        hashed_password = Security.get_hashed_password(password)

        self.assertTrue(Security.check_password(password, hashed_password.decode()))
        self.assertFalse(Security.check_password(wrong_password, hashed_password.decode()))
