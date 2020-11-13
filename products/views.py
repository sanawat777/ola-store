from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hi(request, name):
    return render(request, 'say_hi.html', {'name': name})
