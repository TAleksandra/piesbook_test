from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(' <h1 style="font-size:60px;"> PIESBOOK!</h1>')
# Create your views here.
