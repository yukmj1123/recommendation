from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.template import loader, Context

from tourservice.settings import TEMPLATES
from .models import Busan

from django.http.response import HttpResponseRedirect
from django.db import connection

def mainpage(request):
    return render(request, 'mainpage.html')

def new(request):
    return render(request, 'new.html')
    
def third(request):
    return render(request, 'third.html')

def review(request):
    return render(request, 'review.html')
def listFunc(request):
    bsdata=Busan.objects.all()
    return render(request,'mainpage.html',{"bsdata":bsdata})

