# import numpy as np
import cv2

cap = cv2.VideoCapture(0)


frames = 5
# Capture frame-by-frame


ret, frame = cap.read()

for i in range(frames):
    while(frame is None):
        ret, frame = cap.read()
        print("mess")

    cv2.imwrite("frame{}.jpg".format(i), frame)
    frame = None

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()