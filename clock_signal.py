import time
import pigpio

pi=pigpio.pi()

clk=18
fre=1000

#inicia el reloj
pi.hardware_PWM(clk,fre,500000)

time.sleep(10)
#detine el reloj
pi.hardware_clock(clk,0)

