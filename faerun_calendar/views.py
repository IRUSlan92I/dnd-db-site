from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'faerun_calendar/index.html')
#    return HttpResponse('<h1>Calendar</h1>')

