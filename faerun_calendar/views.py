from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import YearData
from .models import MonthData
from .models import CalendarData
from .models import Event


def day_page(request, year: int, month: int, day: int):
    params = None

    select_suggested = False
    select_only_for_gm = False

    if not params:
        try:
            year_data = YearData.objects.get(number=year)
        except YearData.DoesNotExist:
            params = {'type': 'error', 'error_type': 'year'}

    if not params:
        try:
            year_id = getattr(year_data, 'id')
        except AttributeError:
            params = {'type': 'error', 'error_type': 'year'}

    if not params:
        try:
            month_data = MonthData.objects.get(number=month)
        except MonthData.DoesNotExist:
            params = {'type': 'error', 'error_type': 'month'}

    if not params:
        try:
            month_id = getattr(month_data, 'id')
        except AttributeError:
            params = {'type': 'error', 'error_type': 'month'}

    if not params:
        try:
            is_leap = getattr(year_data, 'is_leap')
        except AttributeError:
            params = {'type': 'error', 'error_type': 'year'}
        else:
            try:
                is_leap_month = getattr(month_data, 'is_leap_month')
            except AttributeError:
                params = {'type': 'error', 'error_type': 'month'}
            else:
                if not is_leap and is_leap_month:
                    params = {'type': 'error', 'error_type': 'month'}

    if not params:
        try:
            events = Event.objects.filter(year=year_id, month=month_id, day=day,
                                          is_suggested=select_suggested, is_only_for_gm=select_only_for_gm
                                          ).order_by('time')
        except Event.DoesNotExist:
            params = {'type': 'error', 'error_type': 'events'}

    if not params:
        try:
            is_oneday = getattr(month_data, 'is_oneday')
        except AttributeError:
            params = {'type': 'error', 'error_type': 'month'}
        else:
            if is_oneday and day != 1 or not 1 <= day <= 30:
                params = {'type': 'error', 'error_type': 'day'}

    if not params:
        params = {
            'type': 'day',
            'year_data': year_data,
            'month_data': month_data,
            'day': day,
            'events': events,
        }

    return render(request, 'faerun_calendar/index.html', params)


def year_page(request, year: int):
    try:
        year_data = YearData.objects.get(number=year)
    except YearData.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')

    month_data = MonthData.objects.all()
    calendar_data = CalendarData.objects.first()
    events = Event.objects.all()

    params = {
        'type': 'year',
        'calendar_data': calendar_data,
        'year_data': year_data,
        'month_data': month_data,
        'month_days': tuple(i+1 for i in range(30)),
        'events': events,
    }

    return render(request, 'faerun_calendar/index.html', params)


def index(request):
    try:
        current_year = getattr(getattr(CalendarData.objects.first(), 'current_year'), 'number')
    except AttributeError:
        current_year = 0

    return year_page(request, current_year)
