from django.shortcuts import redirect, render, get_object_or_404
from .models import Emision
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from random import randrange
from django.contrib import messages


from .utils.factores import FactorFCF,Categorizacion,FactorizacionTipoG

# Create your views here.
@login_required
def mainEmisiones(request):
    Emisiones = Emision.objects.all().order_by('-updated_at')
    cantidadG1,cantidadG2,cantidadG3 = FactorizacionTipoG()

    return render (request, 'mainEmisiones.html',{'Emisiones':Emisiones, 'cantidadG1':cantidadG1,'cantidadG2':cantidadG2,'cantidadG3':cantidadG3},)
@login_required
def categorizacion_pdf(request):
    return render (request, 'categorizacion_PDF.html',{})
@login_required
def procedimientoG1_pdf(request):
    return render (request, 'procedimientoG1_PDF.html',{})
@login_required
def procedimientoG2_pdf(request):
    return render (request, 'procedimientoG2_PDF.html',{})
@login_required
def procedimientoG3_pdf(request):
    return render (request, 'procedimientoG3_PDF.html',{})
@login_required
def graficasEmisiones(request):
    totalEmisiones = Emision.objects.all().count()
    p1Emisiones = Emision.objects.filter(area='Procesos 1').count()
    p2Emisiones = Emision.objects.filter(area='Procesos 2').count()
    p3Emisiones = Emision.objects.filter(area='Procesos 3').count()
    sa1Emisiones = Emision.objects.filter(area='Servicios Auxiliares 1').count()
    sa2Emisiones = Emision.objects.filter(area='Servicios Auxiliares 2').count()
    mes_actual = timezone.now().month
    emisionesDelMes = Emision.objects.filter(fechaReporte__month=mes_actual).count()
    emisionesDelMes1 = Emision.objects.filter(fechaReporte__month=mes_actual-1).count()
    emisionesDelMes2 = Emision.objects.filter(fechaReporte__month=mes_actual-2).count()
    emisionesDelMes3 = Emision.objects.filter(fechaReporte__month=mes_actual-3).count()
    emisionesDelMes4 = Emision.objects.filter(fechaReporte__month=mes_actual-4).count()
    cantidadG1,cantidadG2,cantidadG3 = FactorizacionTipoG()
    context ={
        'cantidadG1' : cantidadG1,
        'cantidadG2' : cantidadG2,
        'cantidadG3' : cantidadG3,
        'totalEmisiones': totalEmisiones,
        'p1Emisiones':  p1Emisiones,
        'p2Emisiones':  p2Emisiones,
        'p3Emisiones':  p3Emisiones,
        'sa1Emisiones':  sa1Emisiones,
        'sa2Emisiones':  sa2Emisiones,
        'emisionesDelMes': emisionesDelMes,
        'emisionesDelMes1': emisionesDelMes1,
        'emisionesDelMes2': emisionesDelMes2,
        'emisionesDelMes3': emisionesDelMes3,
        'emisionesDelMes4': emisionesDelMes4,
    }
    return render (request, 'graficasEmisiones.html',context)

@login_required
def explosimetros(request):
    return render (request, 'explosimetros.html',{})
@login_required
def listaEmisionesTodas(request):
    Emisiones = Emision.objects.all().order_by('-updated_at')
    return render (request, 'areaTodasEmisiones.html',{'Emisiones':Emisiones})
# @login_required
def listaEmisionesPowerBI(request):
    Emisiones = Emision.objects.all().order_by('-updated_at')
    return render (request, 'areaTodasPowerBI.html',{'Emisiones':Emisiones})
@login_required
def listaEmisionesP1(request):
    Emisiones = Emision.objects.filter(area='Procesos 1').order_by('-updated_at')
    return render (request, 'areaP1Emisiones.html',{'Emisiones' : Emisiones})
@login_required
def listaEmisionesP2(request):
    return render (request, 'areaP2Emisiones.html',{})
@login_required
def listaEmisionesP3(request):
    return render (request, 'areaP3Emisiones.html',{})
@login_required
def listaEmisionesSA1(request):
    Emisiones = Emision.objects.filter(area='Servicios Auxiliares 1').order_by('-updated_at')
    return render (request, 'areaP1Emisiones.html',{'Emisiones' : Emisiones})
@login_required
def listaEmisionesSA2(request):
    Emisiones = Emision.objects.filter(area='Servicios Auxiliares 2').order_by('-updated_at')
    return render (request, 'areaP1Emisiones.html',{'Emisiones' : Emisiones})
@login_required
def listaEmisionesG1(request):
    Emisiones = Emision.objects.filter(categoria='G1').order_by('-updated_at')
    return render (request, 'activaG1Emisiones.html',{'Emisiones' : Emisiones})
@login_required
def listaEmisionesG2(request):
    Emisiones = Emision.objects.filter(categoria='G2').order_by('-updated_at')
    return render (request, 'activaG2Emisiones.html',{'Emisiones' : Emisiones})
@login_required
def listaEmisionesG3(request):
    Emisiones = Emision.objects.filter(categoria='G3').order_by('-updated_at')
    return render (request, 'activaG3Emisiones.html',{'Emisiones' : Emisiones})
@login_required
def userEmisiones(request):
    Emisiones = Emision.objects.filter(usuario=request.user).order_by('-updated_at')
    return render (request, 'userEmisiones.html',{'Emisiones' : Emisiones})
@login_required
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
        imagen = request.FILES.get('name_imagenEmision')
        usuario = request.user
        # Para adjuntar imagenes al registro
        # https://www.youtube.com/watch?v=KSFCQud4avc

        emisionSuperada = False;
        FCF = FactorFCF(sustancia,medicion15,presion,instalacion,tamAccesorio,ciclado,ignicion,localizacion,fluido)
        categoria = Categorizacion(FCF)

        emisionNueva = Emision.objects.create(site=site, yacimiento=yacimiento, area= area, sistema=sistema, ubicacion=ubicacion, fuga=fuga,fluido=fluido,sustancia=sustancia,componente=componente,instalacion=instalacion,tamAccesorio=tamAccesorio,medicion=medicion, medicion15=medicion15, presion=presion, ciclado=ciclado,ignicion=ignicion,localizacion=localizacion,usuario=usuario, fechaReporte=fechaReporte, updated_at=updated_at, emisionSuperada=emisionSuperada,FCF=FCF, categoria=categoria, imagen=imagen)
        return redirect ('emisionesPrincipal')
    else:
        return render (request, 'registrarEmisiones.html',{})
@login_required
def detalleEmisiones(request, emision_id ):
    emision = get_object_or_404(Emision,pk=emision_id)
    return render(request, 'detalleEmisiones.html', {'emision' : emision})
@login_required
def eliminarEmisiones(request, emision_id):
    emision = Emision.objects.get(id=emision_id)
    emision.imagen.delete()
    emision.delete()
    messages.success(request,'Actualizado en la base de datos')
    return redirect('/listaMisReportes/')