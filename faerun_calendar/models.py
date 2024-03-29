from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class YearData(models.Model):
    number = models.SmallIntegerField('Number', validators=[
        RegexValidator(r'^-?[1-9]\d{0,3}$', 'Year must be not zero and between -9999 and 9999')
    ])

    @property
    def is_leap(self) -> bool:
        if self.number == 0:
            return False
        elif self.number % 400 == 0:
            return True
        elif self.number % 100 == 0:
            return False
        elif self.number % 4 == 0:
            return True
        return False

    @property
    def next_year(self):
        return YearData.objects.filter(number__gt=self.number).order_by('number').first()

    @property
    def previous_year(self):
        return YearData.objects.filter(number__lt=self.number).order_by('number').last()

    def __str__(self) -> str:
        return f'({self.number}, {self.is_leap})'


class MonthData(models.Model):
    number = models.SmallIntegerField('Number', unique=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(18),
    ])
    name = models.CharField('Name', max_length=64, unique=True)
    folkname = models.CharField('Folkname', max_length=64, blank=True)
    is_oneday = models.BooleanField('IsOneday')
    is_leap_month = models.BooleanField('IsLeapMonth')

    def __str__(self) -> str:
        return f'({self.number}, {self.name}, {self.folkname}, {self.is_oneday}, {self.is_leap_month})'


class CalendarData(models.Model):
    current_day = models.SmallIntegerField('Number', unique=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(30),
    ])
    current_month = models.ForeignKey(MonthData, on_delete=models.CASCADE)
    current_year = models.ForeignKey(YearData, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'({self.current_day}, {self.current_month}, {self.current_year})'


class Event(models.Model):
    day = models.SmallIntegerField('Number', validators=[
        MinValueValidator(1),
        MaxValueValidator(30),
    ])
    month = models.ForeignKey(MonthData, on_delete=models.CASCADE)
    year = models.ForeignKey(YearData, on_delete=models.CASCADE)
    time = models.TimeField('Time')
    title = models.CharField('Title', max_length=250)
    description = models.TextField('Description', max_length=2500)
    is_suggested = models.BooleanField('IsSuggested')
    is_only_for_gm = models.BooleanField('IsOnlyForGm')

    def __str__(self) -> str:
        return f'({self.day}, {self.time}, {self.title})'

