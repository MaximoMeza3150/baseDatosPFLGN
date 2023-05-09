from django.urls import path
from . import views

urlpatterns = [
    path('emisionesFugitivas', views.mainEmisiones, name='emisionesPrincipal'),
    path('registrarEmisiones', views.registrarEmisiones, name='registrarEmisiones'),
]