import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary (value):
     return [int(element) for element in bin(value)[2:].zfill(8)]
n=input()
number = decimal2binary(n)
for i in range(8):
    GPIO.output(dac[i], number[i])
time.sleep(15)
GPIO.output(leds, 0)
GPIO.cleanup()
