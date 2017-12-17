from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
     return render(request, 'landing/landing.html', locals())


def home(request):
     return render(request, 'landing/home.html', locals())