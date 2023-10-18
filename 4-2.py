import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def dec2bin(T):
    for i in range(256):
        for j in range(8):
            GPIO.output(dac[j], decimal2binary(i)[j])
        time.sleep(T/510)
    for i in range(254,0,-1):
        for j in range(8):
            GPIO.output(dac[j], decimal2binary(i)[j])
        time.sleep(T/510)

try:
    T = int(input())
    while(True):
        dec2bin(T)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
