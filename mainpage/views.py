from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *

def mainpage(request):
    return render(request, 'mainpage.html')

def new(request):
    return render(request, 'new.html')
    
def third(request):
    return render(request, 'third.html')

def review(request):
    return render(request, 'review.html')

