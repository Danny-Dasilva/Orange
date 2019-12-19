from __future__ import division 
import numpy as np
import cv2
from Camera import Camera
from Processor import Processor

# cam = cv2.VideoCapture(0)
cam = Camera(0)
p = Processor(cam, 200)

# this is an opencv specific handler for mouse click events
def set_center(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global calibration_point
        calibration_point = [x, y]
        # print(calibration_point)


while(1):
    p.display_img()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.quit()
cv2.destroyAllWindows()


