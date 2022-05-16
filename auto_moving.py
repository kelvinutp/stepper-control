import time
import pigpio

def change_state(pin):
    for b in pin:
        pi.write(b, state[b])
        print("{} {}".format(b,state[b]))
        state[b]=not(state[b])

pi=pigpio.pi()

clk=18

ena=[21,12,8,24,15]
dire=[20,7,25,23,14]

# sensores=[20,21]
#M1,M2,M3,M4,M5

en1=ena[:2]
di1=dire[:2]

pin=en1+di1
# time.sleep(5)
#diccionario de estados de pines (todos salidas)
state={}#pin:state

for a in pin:
    pi.set_mode(a, pigpio.OUTPUT)
    pi.write(a,True)
    state[a]=True

#reloj de 1kHz de frecuencia con 50% duty cycle
pi.hardware_PWM(clk, 1000, 500000)

# # time.sleep(5)
print("Encedido de enable")
for c in en1:
    pi.write(c, not(state[c]))
    print("{} {}".format(c,not(state[c])))

print()
secuencias=10
for z in range(secuencias*2): #hay 5 secuencias 
    #mueve los motores por 3 segundos y cambia de direccion
    change_state(di1)
    
    time.sleep(3)
    print()
    #detenido de enable por 1 segundo
    print('apaga enable')
    change_state(en1)
    time.sleep(1)
    
    print('enciende enable')
    change_state(en1)

    print()

print("Apagado de enable")
for c in en1:
    pi.write(c, state[c])
    print("{} {}".format(c,state[c]))

time.sleep(5)
pi.hardware_PWM(clk, 0, 0)
pi.stop()
print("Fin")
