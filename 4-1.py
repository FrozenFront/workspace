import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
try:
    while(True):
        a = input()
        if str(a) == 'q':
            break
        else:
            try:
                n = float(a)
                try:
                    n = int(a)
                    if n < 0:
                        print("less than zero")
                    elif n > 255:
                        print("too big")
                    else:
                        for i in range(8):
                            GPIO.output(dac[i], decimal2binary(n)[i])
                        print("?????????????? ???????? ?????????? ", 3.3*n/256, " ?")
                except ValueError:
                    print("This is not an integer")
            except ValueError:
                print("This is not a number")    
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
