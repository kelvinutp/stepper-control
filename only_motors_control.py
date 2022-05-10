#!/use/bin/python3
import time
import pigpio
pi=pigpio.pi()

#pines GPIO
clk=18
ena=[15,24,8,12,20]
dire=[14,23,25,7,16]

#frecuencia deseada
freq=1000

pin=ena+dire

state={}

#diccionario de estados de pines de salida
for a in pin:
    pi.set_mode(a,pigpio.OUTPUT)
    pi.write(a,True)
    state[a]=True

#reloj de 1kHz de frecuencia
pi.hardware_PWM(clk,1000,500000)

c=pin[0]
e=0
while c in pin:
    for a in state:
        print("{:<2}: {}".format(a,state[a]))

    c=int(input("pin: "))
    e=time.time()*1000
    #cambia el estado del pin seleccionado
    try:
        d=not(state[c])
        state[c]=d
        pi.write(c,d)
        print()
    except KeyboardInterrupt:
        pi.hardware_PWM(clk,0,0)
    except:
        print("numero de pin incorrecto")

pi.hardware_PWM(clk,0,0)
print("Fin")
