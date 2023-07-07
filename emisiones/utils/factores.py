from ..models import Emision

def FactorFCF(sustancia,medicion15, presion, instalacion,tamAccesorio,ciclado,ignicion,localizacion,fluido):
    if sustancia == "C1 a C4 - Gas":
        FTN_0 = 3
    if sustancia == "C3 a C4 - Líquido condensado (mezcla de líquidos livianos)":
        FTN_0 = 6
    if sustancia == "C5+ - Crudos":
        FTN_0 = 1

    if medicion15 == "LEL ≤ 20":
        FTN_1 = 1
    if medicion15 == "20 < LEL ≤ 60" :
        FTN_1 = 3
    if medicion15 == "LEL > 60":
        FTN_1 = 6
    
    if presion == "Baja presión":
        FTN_2 = 1
    if presion == "Media presión":
        FTN_2 = 3
    if presion == "Alta Presión":
        FTN_2 = 6
    
    FTN = FTN_0 * FTN_1 * FTN_2

    if instalacion == "Unión roscada":
        FPP_0 = 3
    if instalacion == "Unión bridada":
        FPP_0 = 2
    if instalacion == "Sello / junta":
        FPP_0 = 1
    
    if tamAccesorio == 'Menor a 1"' :
        FPP_1 = 3
    if tamAccesorio == 'De 1" a 4"':
        FPP_1 = 2
    if tamAccesorio == 'Mayor a 4"' :
        FPP_1 = 1
    
    if ciclado == "Baja (sin ciclado)"  :
        FPP_2 = 1
    if ciclado == "Medio (térmico o mecánico)":
        FPP_2 = 2
    if ciclado == "Alto (térmico y mecánico)"  :
        FPP_2 = 3
    
    FPP = FPP_0*FPP_1*FPP_2

    if ignicion == "Baja"  :
        FPI_0 = 1
    if ignicion == "Media" :
        FPI_0 = 3
    if ignicion == "Alta"   :
        FPI_0 = 9
    
    if localizacion == "Interior"   :
        FPI_1 = 3
    if localizacion == "Confinado"  :
        FPI_1 = 9
    if localizacion == "Exterior"  :
        FPI_1 = 1
    
    FPI = FPI_0*FPI_1

    if fluido == "C1 - C2 (Gas seco - mezcla)":
        FIA = 27
    if fluido == "NGL" or "C4 - Líquido" or "C3 - Líquido" or "C4 - Gas" or "C3 - Gas" :
        FIA = 9
    if fluido == "Condensado" or "Hot oil" :
        FIA = 1
    
    FCF = FTN+FPP+FPI+FIA

    return(FCF)

def Categorizacion(FCF):
    if FCF <= 11:
        categoria = 'G3'
    if FCF > 12 and FCF <= 72:
        categoria = 'G2' 
    if FCF > 73 and FCF <= 351:
        categoria = 'G1'
    return categoria

def FactorizacionTipoG():
    tipoG1 = Emision.objects.all().filter(categoria='G1')
    tipoG2 = Emision.objects.all().filter(categoria='G2')
    tipoG3 = Emision.objects.all().filter(categoria='G3')

    cantidadG1 = 0
    cantidadG2 = 0
    cantidadG3 = 0

    if(tipoG1==[]):
        cantidadG1 = 0
    else:
        for G1 in tipoG1:
            cantidadG1 = cantidadG1 +1

    if(tipoG2==[]):
        cantidadG2 = 0
    else:
        for G2 in tipoG2:
            cantidadG2 = cantidadG2 +1

    if(tipoG3==[]):
        cantidadG3 = 0
    else:
        for G3 in tipoG3:
            cantidadG3 = cantidadG3 +1

    return cantidadG1,cantidadG2,cantidadG3