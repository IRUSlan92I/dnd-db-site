from django.shortcuts import render
from .models import CalendarData
from .models import MonthData


def index(request):
    def is_leap_year(year) -> bool:
        if year == 0:
            return False
        elif year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        return False

    calendar_data = CalendarData.objects.first()
    month_data = MonthData.objects.all()

    year = 1492

    params = {
        'calendar_data': calendar_data,
        'month_data': month_data,
        'month_days': tuple(i+1 for i in range(30)),
        'year': year,
        'is_leap_year': is_leap_year(year),
    }

    return render(request, 'faerun_calendar/index.html', params)
