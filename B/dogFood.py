import RPi.GPIO as GPIO
import time

class runDogFood:

    def __init__(self):
        # Sets up servo
        # Uses pin 26
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        self.p = GPIO.PWM(26, 50)
        self.p.start(0)
        print("starting")

    def feed(self, angle):
        print("starting rotation")

        # Math to find angle 
        duty = angle / 18 + 2
        try:
            # Rotation, wait, then reset
            self.p.ChangeDutyCycle(duty)
            time.sleep(1)
            self.p.ChangeDutyCycle(0)
        except KeyboardInterrupt:
            self.p.stop()
            GPIO.cleanup()
        print("done!")

    # To actually do the rotation
    def giveFood(self):
        self.feed(180)
        self.feed(25)
        time.sleep(3)
        self.feed(180)
        print("Food Dispensed!")

    def startThisThread(self):
        obj = runDogFood()