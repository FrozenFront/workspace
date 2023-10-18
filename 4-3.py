import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
p = GPIO.PWM(9, 0.5)
p.start(1)
try:
    while(True):
        n = int(input())
        p.ChangeDutyCycle(n)

        print(3.3*n/100, " ?")
finally:
    GPIO.output(21,0)
    GPIO.cleanup()
