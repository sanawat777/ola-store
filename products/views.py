from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.


def say_hi(request, name):
    return render(request, 'say_hi.html', {'name': name})


def show_time(request, time):
    now = timezone.now()
    return render(request, 'show_time.html', {'time': now})
