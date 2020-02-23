import RPi.GPIO as GPIO
from time import sleep 

GPIO_PUMP = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(GPIO_PUMP, GPIO.OUT, initial=GPIO.LOW) 
while True: 
 GPIO.output(GPIO_PUMP, GPIO.HIGH)
 print('high')
 sleep(3)
 GPIO.output(GPIO_PUMP, GPIO.LOW) 
 print('low')
 sleep(1) 