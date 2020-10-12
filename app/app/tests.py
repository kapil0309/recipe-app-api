from djangorest.test import TestCase

from app.calc import add

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Tets that two  numbers are added together"""
        self.assertEqual(add(3,8), 11)