from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def horariosAnteriores(request):
    return render(request, 'horariosAnteriores.html')