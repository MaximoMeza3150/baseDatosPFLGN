from django.shortcuts import render

# Create your views here.

def mainEmisiones(request):
    return render (request, 'mainEmisiones.html',{})