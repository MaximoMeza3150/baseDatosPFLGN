from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('busquedaDatasheets', views.mainEquipos, name='DatasheetEquipos')
]