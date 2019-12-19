from __future__ import division
import numpy as np
import cv2

class Camera:
    def __init__(self, port):
        self.cam = cv2.VideoCapture(port)
        

    def quit(self):
        self.cam.release()


    def get_frame(self):
        ret, frame = self.cam.read()
        return frame
        
        
    def change_exposure(exposure_val):
        cam.set(cv2.CAP_PROP_EXPOSURE, exposure_val)


    def change_brightness(brightness_val):
        cam.set(cv2.CAP_PROP_BRIGHTNESS, brightness_val)
    
    
    def change_contrast(contrast_val):
        cam.set(cv2.CAP_PROP_CONTRAST, contrast_val)
    
    
    def change_saturation(saturation_val):
        cam.set(cv2.CAP_PROP_SATURATION, saturation_val)
    
    def invert_image(image):
        return cv2.bitwise_not(image)
    
    
    def flip_image_vert(image):
        return cv2.flip(image, 0)
    
    
    def flip_image_hor(image):
        return cv2.flip(image, 1)