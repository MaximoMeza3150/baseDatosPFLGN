from django.shortcuts import redirect, render
from .models import Emision
from django.contrib.auth.models import User
import datetime

from .utils.factores import FactorFCF,Categorizacion,FactorizacionTipoG

# Create your views here.

def mainEmisiones(request):
    Emisiones = Emision.objects.all().order_by('-updated_at')
    cantidadG1,cantidadG2,cantidadG3 = FactorizacionTipoG()

    return render (request, 'mainEmisiones.html',{'Emisiones':Emisiones, 'cantidadG1':cantidadG1,'cantidadG2':cantidadG2,'cantidadG3':cantidadG3},)

def explosimetros(request):
    return render (request, 'explosimetros.html',{})

def categorizacion_pdf(request):
    return render (request, 'categorizacion_PDF.html',{})
def procedimientoG1_pdf(request):
    return render (request, 'procedimientoG1_PDF.html',{})
def procedimientoG2_pdf(request):
    return render (request, 'procedimientoG2_PDF.html',{})
def procedimientoG3_pdf(request):
    return render (request, 'procedimientoG3_PDF.html',{})
def graficasEmisiones(request):
    return render (request, 'graficasEmisiones.html',{})

def registrarEmisiones(request):
    if request.method == 'POST':
        site = request.POST.get('name_site', '')
        yacimiento = request.POST.get('name_yacimiento', '')
        area = request.POST.get('name_area', '')
        sistema = request.POST.get('name_sistema', '')
        ubicacion = request.POST.get('name_ubicacion', '')
        fuga = request.POST.get('name_fuga', '')
        fluido = request.POST.get('name_fluido', '')
        sustancia = request.POST.get('name_sustancia', '')
        componente = request.POST.get('name_componente', '')
        instalacion = request.POST.get('name_instalacion', '')
        tamAccesorio = request.POST.get('name_tamAccesorio', '')
        medicion = request.POST.get('name_medicion', '')
        medicion15 = request.POST.get('name_medicion15', '')
        presion = request.POST.get('name_presion', '')
        ciclado = request.POST.get('name_ciclado', '')
        ignicion = request.POST.get('name_ignicion', '')
        localizacion = request.POST.get('name_localizacion', '')
        fechaReporte = request.POST.get('name_fechaReporte', '')
        updated_at = datetime.datetime.now()
        usuario = request.user
        # Para adjuntar imagenes al registro
        # https://www.youtube.com/watch?v=KSFCQud4avc

        emisionSuperada = False;
        FCF = FactorFCF(sustancia,medicion15,presion,instalacion,tamAccesorio,ciclado,ignicion,localizacion,fluido)
        categoria = Categorizacion(FCF)

        emisionNueva = Emision.objects.create(site=site, yacimiento=yacimiento, area= area, sistema=sistema, ubicacion=ubicacion, fuga=fuga,fluido=fluido,sustancia=sustancia,componente=componente,instalacion=instalacion,tamAccesorio=tamAccesorio,medicion=medicion, medicion15=medicion15, presion=presion, ciclado=ciclado,ignicion=ignicion,localizacion=localizacion,usuario=usuario, fechaReporte=fechaReporte, updated_at=updated_at, emisionSuperada=emisionSuperada,FCF=FCF, categoria=categoria)

        return redirect ('emisionesPrincipal')
    else:
        return render (request, 'registrarEmisiones.html',{})