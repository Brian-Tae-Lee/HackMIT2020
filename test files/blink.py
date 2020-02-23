import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

Output_PIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(Output_PIN, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
while True: # Run forever
 GPIO.output(Output_PIN, GPIO.HIGH) # Turn on
 print('aaa')
 sleep(2) # Sleep for 1 second
 GPIO.output(Output_PIN, GPIO.LOW) # Turn off
 print('aaab')
 sleep(2) # Sleep for 1 second