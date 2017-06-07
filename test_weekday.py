from unittest import TestCase
from weekday import weekday

class TestWeekday(TestCase):
    def test_weekday(self):
        self.assertEqual(2, weekday(7,6,2017))


