from unittest import TestCase

from weekday import weekday


class TestWeekday(TestCase):
    def test_weekdayNone(self):
        self.assertIsNone(weekday(29, 2, 2017))
        self.assertIsNone(weekday(30, 2, 2017))
        self.assertIsNone(weekday(31, 2, 2017))
        self.assertIsNone(weekday(32, 1, 2016))
        self.assertIsNone(weekday(32, -1, -2))
        self.assertIsNone(weekday(0, 1, 2016))
        self.assertIsNone(weekday(0, 23, 2016))
        self.assertIsNone(weekday(1, 23, 2016))
        self.assertIsNone(weekday(1, 13, 2016))
        self.assertIsNone(weekday(1, 13, 1500))
        self.assertIsNone(weekday(1, 13, -1500))
        self.assertIsNone(weekday(0, 0, 0))
        self.assertIsNone(weekday(0, 0, 0))

    def test_weekday0(self):
        self.assertEqual(0, weekday(29, 2, 2016))
        self.assertEqual(0, weekday(6, 1, 2003))
        self.assertEqual(0, weekday(23, 2, 2004))
        self.assertEqual(0, weekday(11, 1, 1943))

    def test_weekday1(self):
        self.assertEqual(1, weekday(3, 1, 2033))
        self.assertEqual(1, weekday(14, 1, 2030))

    def test_weekday2(self):
        self.assertEqual(2, weekday(31, 12, 2025))
        self.assertEqual(2, weekday(29, 2, 2012))

    def test_weekday3(self):
        self.assertEqual(3, weekday(25, 12, 2025))

    def test_weekday4(self):
        self.assertEqual(4, weekday(24, 1, 55))
        self.assertEqual(4, weekday(7, 1, 1))
        self.assertEqual(4, weekday(24, 6, 1))

    def test_weekday5(self):
        self.assertEqual(5, weekday(12, 6, 3999))
        self.assertEqual(5, weekday(3, 3, 1492))
        self.assertEqual(5, weekday(2, 6, 966))

    def test_weekday6(self):
        self.assertEqual(6, weekday(1, 1, 1))
        self.assertEqual(6, weekday(24, 9, 2023))
        self.assertEqual(6, weekday(15, 2, 2015))
        self.assertEqual(6, weekday(13, 1, 2013))
        self.assertEqual(6, weekday(28, 4, 2013))
