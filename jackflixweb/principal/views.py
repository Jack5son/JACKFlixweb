from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import os
# Create your views here.


def index(request):
    #Procura dentro de templates
    return render(request, 'principal/index.html')

