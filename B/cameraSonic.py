#Libraries
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import cv2

Output_PIN = 21


# Create CSI Camera
camera = PiCamera()
camera.rotation = 0

# Frame number
fNum = 0

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 15
GPIO_ECHO = 23
GPIO_LED = 4

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Output_PIN, GPIO.OUT, initial=GPIO.LOW)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

led_power = False
while True:
    # Buffer so that random misfires 
    # do not result in detection
    loop = 0
    for i in range(5):
        dist = distance()
        # RHS ^ => dist detection range ^
        if dist < 20:
            loop += 1
    
    # Threshold for detection is 5 consecutive frames
    if loop == 5:
        print('detected!!!')

        # USB Camera
        cap = cv2.VideoCapture(0)

        # CSI Camera
        camera.start_preview()

        # Capture frame-by-frame
        ret, frame = cap.read()
    
        # Takes Pictures, stores them in respective image names
        camera.capture("webapp/static/CSI{}.jpg".format(fNum))
        cv2.imwrite("webapp/static/USB{}.jpg".format(fNum), frame)

        # increment counter for bird pics
        fNum += 1

        # CSI Camera
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        camera.stop_preview()

        # Restart search
        if not led_power:
            GPIO.output(GPIO_LED, GPIO.HIGH)
        
        print('Bird Picture Captured!')
        time.sleep(60)
    else:
        print('not detected!!!')

        # Restart search
        if led_power:
            GPIO.output(GPIO_LED, GPIO.LOW)
        
        time.sleep(.1)