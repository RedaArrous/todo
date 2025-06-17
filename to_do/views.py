from django.http import HttpResponse 
from django.urls import reverse
from django.shortcuts import render


def landing_view(request):
    return render(request, 'to_do/landing.html')
