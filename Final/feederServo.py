import RPi.GPIO as GPIO
from time import sleep

Output_PIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(Output_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(Output_PIN, GPIO.HIGH)
print('on')
sleep(2)
GPIO.output(Output_PIN, GPIO.LOW)
print('off')
sleep(2)