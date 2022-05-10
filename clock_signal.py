import time
import pigpio

pi=pigpio.pi()

#GPIO pin
clk=18

#desired frecuency
fre=1000

#Start clock signal
pi.hardware_PWM(clk,fre,500000)

time.sleep(10)

#stops clock signal
pi.hardware_clock(clk,0)

