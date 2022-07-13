from django.test import TestCase
from .models import FaerunDate


class FaerunDateTestCase(TestCase):
    class TestDate:
        def __init__(self, date: FaerunDate, repr: str, is_leap_year: bool, is_valid: bool):
            self.date = date
            self.repr = repr
            self.is_leap_year = is_leap_year
            self.is_valid = is_valid

    def setUp(self):
        self.dates = (
            FaerunDateTestCase.TestDate(FaerunDate(0, 0, 0), 'FaerunDate(0, 0, 0)', False, False),
            FaerunDateTestCase.TestDate(FaerunDate(1, -1, 1), 'FaerunDate(1, -1, 1)', False, False),
            FaerunDateTestCase.TestDate(FaerunDate(1, 1, 1), 'FaerunDate(1, 1, 1)', False, True),
            FaerunDateTestCase.TestDate(FaerunDate(4, 1, 1), 'FaerunDate(4, 1, 1)', True, True),
            FaerunDateTestCase.TestDate(FaerunDate(4, -1, 1), 'FaerunDate(4, -1, 1)', True, False),
            FaerunDateTestCase.TestDate(FaerunDate(4, 0, 1), 'FaerunDate(4, 0, 1)', True, False),
            FaerunDateTestCase.TestDate(FaerunDate(4, 19, 1), 'FaerunDate(4, 19, 1)', True, False),
            FaerunDateTestCase.TestDate(FaerunDate(4, 1, -1), 'FaerunDate(4, 1, -1)', True, False),
            FaerunDateTestCase.TestDate(FaerunDate(4, 1, 0), 'FaerunDate(4, 1, 0)', True, False),
            FaerunDateTestCase.TestDate(FaerunDate(4, 1, 31), 'FaerunDate(4, 1, 31)', True, False),
            FaerunDateTestCase.TestDate(FaerunDate(4, 2, 2), 'FaerunDate(4, 2, 2)', True, False),
            FaerunDateTestCase.TestDate(FaerunDate(4, 1, 2), 'FaerunDate(4, 1, 2)', True, True),
            FaerunDateTestCase.TestDate(FaerunDate(1, 11, 1), 'FaerunDate(1, 11, 1)', False, False),
            FaerunDateTestCase.TestDate(FaerunDate(4, 11, 1), 'FaerunDate(4, 11, 1)', True, True),
        )

    def test_repr(self):
        for date in self.dates:
            self.assertEqual(date.date.__repr__(), date.repr)

    def test_leap(self):
        for date in self.dates:
            self.assertEqual(date.date.is_leap_year, date.is_leap_year, date.date.__repr__())

    def test_valid(self):
        for date in self.dates:
            self.assertEqual(date.date.is_valid, date.is_valid, date.date.__repr__())


