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


# while(True):
#     ret, frame = cam.read()
#     cv2.namedWindow('image')
#     cv2.setMouseCallback('image', set_center)

#     box = draw_cnts(frame)
    
#     cnts_center = target_dist_to_center(box)
#     if cnts_center is not None:
#         print("Horizontal Distance: " + str(cnts_center[0]) + ", Vertical Distance: " + str(cnts_center[1]))
#     target_dist_to_center(box)
#     # cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
#     cv2.imshow('image', frame)

# cam.release()
# cv2.destroyAllWindows()

while(1):
    p.display_img()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.quit()
cv2.destroyAllWindows()


