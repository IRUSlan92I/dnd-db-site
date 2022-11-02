from django.contrib import admin

from .models import YearData
from .models import MonthData
from .models import Event
from .models import CalendarData

admin.site.register(YearData)
admin.site.register(MonthData)
admin.site.register(Event)
admin.site.register(CalendarData)

