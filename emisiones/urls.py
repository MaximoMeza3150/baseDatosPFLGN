from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('emisionesFugitivas/', views.mainEmisiones, name='emisionesPrincipal'),
    path('registrarEmisiones/', views.registrarEmisiones, name='registrarEmisiones'),
    path('explosimetros/', views.explosimetros, name='explosimetros'),
    path('categorizacionEmisiones/', views.categorizacion_pdf, name='categorizacionEmisiones'),
    path('procedimientoG1/', views.procedimientoG1_pdf, name='procedimientoG1'),
    path('procedimientoG2/', views.procedimientoG2_pdf, name='procedimientoG2'),
    path('procedimientoG3/', views.procedimientoG3_pdf, name='procedimientoG3'),
    path('graficasEmisiones/', views.graficasEmisiones, name='graficasEmisiones'),
    path('listaEmisionesTodas/', views.listaEmisionesTodas, name='listaEmisionesTodas'),
    path('listaEmisionesP1/', views.listaEmisionesP1, name='listaEmisionesP1'),
    path('listaEmisionesP2/', views.listaEmisionesP2, name='listaEmisionesP2'),
    path('listaEmisionesP3/', views.listaEmisionesP3, name='listaEmisionesP3'),
    path('listaEmisionesSA1/', views.listaEmisionesSA1, name='listaEmisionesSA1'),
    path('listaEmisionesSA2/', views.listaEmisionesSA2, name='listaEmisionesSA2'),
    path('listaEmisionesG1/', views.listaEmisionesG1, name='listaEmisionesG1'),
    path('listaEmisionesG2/', views.listaEmisionesG2, name='listaEmisionesG2'),
    path('listaEmisionesG3/', views.listaEmisionesG3, name='listaEmisionesG3'),
    path('listaMisReportes/', views.userEmisiones, name='listaMisReportes'),
    path('listaPowerBI/', views.listaEmisionesPowerBI, name='listaEmisionesPowerBI'),
    path('detalleEmisiones/<int:emision_id>', views.detalleEmisiones, name='detalleEmisiones'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)