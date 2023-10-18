import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2,3,4,17,27,22,10,9]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
gpio.setup(led, gpio.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def leds(value):
    for i in range(8,0,-1):
        if i*32-1 <= value:
            return decimal2binary(2**i-1)
    return decimal2binary(0)

def adc():
    value = 0
    for k in range (7,-1,-1):
        gpio.output(dac,decimal2binary(2**k+value))
        time.sleep(0.0008)
        if gpio.input(comp) == 0:
            value += 2**k
    return value

try:
    while (True):
        gpio.output(led,leds(adc()))
except KeyboardInterrupt:
    print("\n Программа остановленна с клавиатуры")
finally:
    gpio.output(dac,0)
    gpio.cleanup()
