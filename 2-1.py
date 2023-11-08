import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds=[2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)
while(1):
 N=int(input('количество повторов='))
for j in range(N):
        for i in range(8):
            GPIO.output(leds[i],1)
            time.sleep(0.2)
            GPIO.output(leds[i],0)
GPIO.output(leds, 0)
GPIO.cleanup()
