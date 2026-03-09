from django.http import HttpResponse
from django.shortcuts import render
from Produto.models import Produto

def home(request):
    return render(request, 'base.html')
