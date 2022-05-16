import time
import pigpio
pi=pigpio.pi()

clk=18

freq_min=600
freq_max=1000

time.sleep(15)
pi.write(15,False)
pi.write(14,True)

#arranque
for a in range(freq_min,freq_max+1,100):
    print('Frecuencia: ',a)
    pi.hardware_PWM(clk,a,500000)
    time.sleep(0.5)

#estable
print('estable')
pi.write(15,False)
time.sleep(3)

#frenado
for a in range(freq_max,freq_min-1,-100):
    print('Frecuencia: ',a)
    pi.hardware_PWM(clk,a,500000)
    time.sleep(0.5)
    

pi.write(15,True)
pi.hardware_PWM(clk,0,0)
