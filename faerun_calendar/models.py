from django.db import models


class FaerunDate:
    LAST_MONTH = 18
    LEAP_MONTH = 11
    ONE_DAY_MONTHS = (2, 6, 10, 11, 14, 17)
    LAST_DAY = 30

    def __init__(self, year: int,  month: int,  day: int):
        self.year = year
        self.month = month
        self.day = day
        self.is_leap_year = self._is_leap_year()
        self.is_valid = self._is_valid()

    def __repr__(self):
        return f'{type(self).__name__}({self.year}, {self.month}, {self.day})'

    def _is_leap_year(self) -> bool:
        if self.year == 0:
            return False
        elif self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def _is_valid(self) -> bool:
        if self.year == 0:
            return False

        if not 0 < self.month <= FaerunDate.LAST_MONTH:
            return False

        if not self.is_leap_year and self.month == self.__class__.LEAP_MONTH:
            return False

        if not 0 < self.day <= FaerunDate.LAST_DAY:
            return False

        if self.day > 1 and self.month in FaerunDate.ONE_DAY_MONTHS:
            return False

        return True


class CalendarData(models.Model):
    current_year = models.SmallIntegerField('CurrentYear')
    current_month = models.SmallIntegerField('CurrentMonth')
    current_day = models.SmallIntegerField('CurrentDay')
    leap_month = models.SmallIntegerField('LeapMonth')

    def __str__(self):
        return f'({self.current_year}, {self.current_month}, {self.current_day}, {self.leap_month})'


class MonthData(models.Model):
    number = models.SmallIntegerField('Number', unique=True)
    name = models.CharField('Name', max_length=64, unique=True)
    folkname = models.CharField('Folkname', max_length=64, blank=True)
    is_oneday = models.BooleanField('IsOneday')

    def __str__(self):
        return f'({self.number}, {self.name}, {self.folkname}, {self.is_oneday})'


class Event(models.Model):
    year = models.SmallIntegerField('Year')
    month = models.SmallIntegerField('Month')
    day = models.SmallIntegerField('Day')
    time = models.TimeField('Time')
    title = models.CharField('Title', max_length=250)
    description = models.TextField('Description', max_length=2500)

    def __str__(self):
        return f'({self.year}, {self.month}, {self.day}, {self.time}, {self.title})'
