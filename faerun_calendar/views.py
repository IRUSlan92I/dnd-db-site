from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

from .models import YearData
from .models import MonthData
from .models import CalendarData
from .models import Event


def year_page(request, year: int):
    try:
        year_data = YearData.objects.get(number=year)
    except YearData.DoesNotExist:
        return HttpResponseNotFound("<h1>404 Not Found</h1>")

    month_data = MonthData.objects.all()
    calendar_data = CalendarData.objects.first()

    params = {
        'calendar_data': calendar_data,
        'year_data': year_data,
        'month_data': month_data,
        'month_days': tuple(i+1 for i in range(30)),
    }

    return render(request, 'faerun_calendar/index.html', params)


def index(request):
    calendar_data = CalendarData.objects.first()

    try:
        current_year = getattr(getattr(CalendarData.objects.first(), 'current_year'), 'number')
    except AttributeError:
        current_year = 0

    return year_page(request, current_year)
