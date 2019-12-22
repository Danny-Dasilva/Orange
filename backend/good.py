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
        print(y, x)
        print(frame[y,x].tolist())
        CVProcessor.set_eyedropper(frame[y,x].tolist())

for img,mask,boxes in CVProcessor.process():
    
    for box in boxes:
        cv2.drawContours(mask,[box],0,(0,127,255),2)
    cv2.imshow('img',img)
    cv2.imshow('filter',mask)
    cv2.setMouseCallback('img', on_mouse_click, img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()