from math import degrees
from django.shortcuts import render
# from django.http import HttpResponse
import pigpio
from control.calibracion2 import gryphon

# Create your views here.
m=[a for a in range(6)]

#welcome Page
#inicializando motores
m[1]=gryphon(14,15,2,3,270,[6,13])
m[2]=gryphon(23,24,4,17,165,[19,26])
m[3]=gryphon(25,8,27,22,300,[21])
m[4]=gryphon(7,12,10,9,290)
m[5]=gryphon(16,20,11,5,290)

def index(request):
    for a in range(1,6):
        m[a].show_GPIO()
        
    context={
        'title':"Tesis",
        'msg':"Haciendo pruebas",
        'boton':'Next'
    }
    return render(request,'project.html',context)

#motors control page
def motors(request,pk=0,w=''):
    a=range(1,6)
    context={
        'motors':a
    }
    if pk!=0:
        if w=='cw':
            estado=True
        elif w=='ccw':
            estado=False
        else:
            estado=''
        m[pk].change('dir',estado)
        m[pk].show_state()
        
    return render(request,'controles.html',context)

#calibracion
def calibracion(request,z=0):
    print('calibracion')
    a=range(1,6)
    context={
        'motors':a
    }
    if z!=0:
        print('calibracion de motor: ',z)
        # m[z].calibracion()
    return render(request,'controles.html',context)

#variacion de frecuencia
def vari(request,y=0):
    print('movimiento con variacion de frecuencia')
    a=range(1,6)
    context={
        'motors':a
    }

    return render(request,'controles.html',context)

#desplazamiento
def move(request,z=0):
    
    print("movimiento sin variacion de frecuencia")#,degree)
    a=range(1,6)
    context={
        'motors':a
    }

    return render(request,'controles.html',context)

#exit page
def fin(request):
    print('Fin')
    return render(request,'fin.html')