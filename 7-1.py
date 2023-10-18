import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2,3,4,17,27,22,10,9]
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
comp = 14
troyka = 13
GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    n = 0
    for i in range(8):
        a[i] = 1
        GPIO.output(dac, a)
        time.sleep(0.01)
        compvalue = GPIO.input(comp)
        if compvalue == 1:
            a[i] = 0
        else:
            n += 2**(7-i)          
    return n

def valtoleds(value):
    for i in range(8):
        GPIO.output(led[i],decimal2binary(value)[i])

count = 0
try:
    troyka_value_list = []
    GPIO.output(troyka,1)
    troyka_value = 0
    t1 = time.time()
    while troyka_value<(207):
        troyka_value = adc()
        troyka_value_list.append(troyka_value)
        valtoleds(troyka_value)
        count+=1
        print("In decimal -> ", troyka_value, " // In Voltage -> ", round(((troyka_value/255)*3.3),5), " // Time from start -> ", (time.time()-t1), end="\n")
    GPIO.output(troyka,0)
    t2 = time.time()
    while troyka_value>(166):
        troyka_value = adc()
        troyka_value_list.append(troyka_value)
        valtoleds(troyka_value)
        count+=1
        print("In decimal -> ", troyka_value, " // In Voltage -> ", round(((troyka_value/255)*3.3),5), " // Time from start -> ", (time.time()-t1), end="\n")
    t3 = time.time()
    t_fromstart = t3-t1
    print("finally")

    plt.plot(troyka_value_list)
    plt.show()
    troyka_value_list_str = [str(item) for item in troyka_value_list]

    with open("mine-data.txt", "w") as data:
        data.write("\n".(troyka_value_list_str, " <- значение в десятичной системе"))
    
    details = [str(round(1/(t_fromstart/count), 2)), str(round(3.3/256, 5))]
    with open("mine-settings.txt", "w") as set:
        set.write(str(round(1/(t_fromstart/count), 2)), " <- частота дискретизации ", "\n", str(round(3.3/256, 5)), " <- шаг квантования")
    
    print("Summ of time -> ", round(t_fromstart, 2), " // Middle of time between uses -> ", round(t_fromstart/count, 5), " // Middle of step discretitation -> ", round(count/t_fromstart, 5), " // Step of kvantovanie -> ", round(3.3/255,5))

finally:
    GPIO.output(dac,0)
    GPIO.output(led,0)
    GPIO.cleanup()
