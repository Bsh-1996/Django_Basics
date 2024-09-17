from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def home(request):
    person = {'name': 'behrouz'}
    return render(request, 'home.html', person)