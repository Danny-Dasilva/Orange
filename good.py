import cv2
from Camera import Camera
from CVProcessing import tapePos
from time import sleep
import random

## Read
cam = Camera(0)
CVProcessor = tapePos(cam)

def on_mouse_click (event, x, y, flags, frame):
    global CVProcessor
    if event == cv2.EVENT_LBUTTONUP:
        CVProcessor.set_eyedropper(frame[y,x].tolist())

for hsv,img,green in CVProcessor.process():
    
    cv2.setMouseCallback('img', on_mouse_click, img)
    cv2.imshow('img',img)
    cv2.imshow('hsv',hsv)
    cv2.imshow('filter',green)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()