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
    num=0
    a = [1,0,0,0,0,0,0,0]
    for i in range(8):
        gpio.output(dac,a)
        time.sleep(0.007)
        v_comp = gpio.input(comp)
        if v_comp == 1:
            a[i]=0
        else:
            a[i]=1
            num += 2**(7-i)
    print("Десятичное число, пропорциональное напряжению клемме S тройка-модуля = ", num, "Напряжение соответсвенно равно = ", (num/256)*3.3)


try:
    while (True):
        abc()
except KeyboardInterrupt:
    print("\n Программа остановленна с клавиатуры")
finally:
    gpio.output(dac,0)
    gpio.cleanup()
