from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    if User.is_authenticated:
        return render(request,"index.html")
    else:
        return redirect('signup')


def signup(request):
    if request.method == 'GET':
        form = CustomUserCreationForm
        return render(request, 'signup.html', {'form': form})
    else:
        form = CustomUserCreationForm(request.POST)
        if request.POST['password1'] == request.POST ['password2']:
                if form.is_valid():
                    user = form.save()
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request,'signup.html',{
                        'form': form,
                        'error': 'El usuario ya existe'
                })
        else:
            return render(request,'signup.html',{
                'form': form,
                'error': 'Las contraseñas no coinciden'
            })

def signout (request):
    logout(request)
    return redirect('index')

def signin (request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user == None:
            return render(request, 'signin.html',{
                'form':     AuthenticationForm,
                'error':    'Usuario y/o contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('index')


def mainEquipos(request):
    return render (request, 'mainEquipos.html',{})