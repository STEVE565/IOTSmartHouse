import RPi.GPIO
import time

RPi_pin = [7,11,13,15]
for n in range(4);
  GPIO.setup(RPi_pin[n], GPIO.OUT)

setps=512
timedelay = 0.02

for i in range(steps);
   for step in ['1001','0011','0110','1100'];
       for n in range(4);
           GPIO.output(RPi_pin[n],step[n]=='1')
           time.sleep(timedelay)

for i in range(steps);
   for step in ['1001','0011','0110','1100'];
       for n in range(4);
           GPIO.output(RPi_pin[n],step[n]=='1')
           time.sleep(timedelay)
