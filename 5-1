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
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = decimal2binary(value)
    gpio.output(dac,signal)
    return signal

def abc():
    for i in range (256):
        signal = decimal2binary(i)
        gpio.output(dac, signal)
        time.sleep(0.005)
        v_comp = gpio.input(comp)
        if v_comp == 1:
            print("Десятичное число, пропорциональное напряжению клемме S тройка-модуля = ", i)
            print("Напряжение соответсвенно равно = ", (i/255)*3.3)
            break
    return i

try:
    while (True):
        abc()

finally:
    gpio.output(dac,0)
    gpio.cleanup()
