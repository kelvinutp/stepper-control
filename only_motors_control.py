import time
import pigpio
pi=pigpio.pi()

#GPIO pins
clk=18
#enable pins start/stop movement
ena=[15,24,8,12,20]
#dire pins change rotation  (clockwise/anticlockwise)
dire=[14,23,25,7,16]

#desired frequency
freq=1000

pin=ena+dire

state={}

#setting initial pin state=True
for a in pin:
    pi.set_mode(a,pigpio.OUTPUT)
    pi.write(a,True)
    state[a]=True

#starting clock signal
pi.hardware_PWM(clk,freq,500000)

c=pin[0]
e=0
while c in pin:
    #print pin and state
    for a in state:
        print("{:<2}: {}".format(a,state[a]))

    #changing desired pin state
    c=int(input("pin: "))
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
