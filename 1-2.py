import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
while True:
    GPIO.output(20,GPIO.input(25))
