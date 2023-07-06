from django.urls import path
from . import views

urlpatterns = [
    path('emisionesFugitivas/', views.mainEmisiones, name='emisionesPrincipal'),
    path('registrarEmisiones/', views.registrarEmisiones, name='registrarEmisiones'),
    path('explosimetros/', views.explosimetros, name='explosimetros'),
    path('categorizacionEmisiones/', views.categorizacion_pdf, name='categorizacionEmisiones'),
    path('procedimientoG1/', views.procedimientoG1_pdf, name='procedimientoG1'),
    path('procedimientoG2/', views.procedimientoG2_pdf, name='procedimientoG2'),
    path('procedimientoG3/', views.procedimientoG3_pdf, name='procedimientoG3'),
    path('graficasEmisiones/', views.graficasEmisiones, name='graficasEmisiones'),
]