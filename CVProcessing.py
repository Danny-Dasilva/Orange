import cv2
from threading import Thread
import numpy as np
from time import sleep
import enum

class targetRegion(enum.Enum):
    topLeft = 0
    top = 1
    topRight = 2
    right = 3
    bottomRight = 4
    bottom = 5
    bottomLeft = 6
    left = 7
    center = 8

class tapePos:
    def __init__(self,camObject):
        self.cam = camObject
        self.exposure = 157 #ms #ON CORAL
        self.white_balance = 100 #CHANGE #ON CORAL
        self.hue = (0,0) #Pixel
        self.saturation = (0,0) #Pixel
        self.value = (255,255) #Pixel
        self.erosion = 0 #CHANGE
        self.dilation = 0 #CHANGE
        self.target_area = 4000
        self.target_fullness = 0 #CHANGE
        self.target_aspect_ratio = 0 #CHANGE
        self.target_region = targetRegion.center
        self.eyedropper_mode = "max"

    def process(self):
        while True:
            sleep(0.03)
            img = self.cam.get_frame()
            ## convert to hsv
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            mask = cv2.inRange(hsv, (self.hue[0], self.saturation[0], self.value[0]), (self.hue[1], self.saturation[1],self.value[1]))
            
            contours,hierarchy = cv2.findContours(mask, 1, 2)
            colorMask = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
            boxes = []
            for cnt in contours:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                if cv2.contourArea(box) > self.target_area:
                    boxes.append(box)

            yield img,colorMask,boxes
            ## save 
    
    def read_pipeline(self):
        pass

    def source_image(self):
        pass

    def set_leds(self):
        pass

    def set_orientation(self):
        pass

    def set_exposure(self):
        pass

    def read_eyedropper(self):
        pass

    def set_eyedropper(self,hsv_value):
        print(hsv_value)
        hue = hsv_value[0]
        saturation = hsv_value[1]
        value = hsv_value[2]

        hueRange = self.hue
        saturationRange = self.saturation
        valueRange = self.value

        if self.eyedropper_mode == "min":
            hueRange = [hue,self.hue[1]]
            saturationRange = [saturation,self.saturation[1]]
            valueRange = [value,self.value[1]]

        elif self.eyedropper_mode == "max":
            hueRange = [self.hue[0],hue]
            saturationRange = [self.saturation[0],saturation]
            valueRange = [self.value[0],value]
        
        self.clampHSV(hueRange)
        self.clampHSV(saturationRange)
        self.clampHSV(valueRange)

        self.set_hue(hueRange)
        self.set_saturation(saturationRange)
        self.set_value(valueRange)

    def set_min(self):
        self.eyedropper_mode = "min"

    def set_max(self):
        self.eyedropper_mode = "max"

    def set_hue(self,hue):
        self.hue = hue

    def set_saturation(self,saturation):
        self.saturation = saturation

    def set_value(self, value):
        self.value = value

    def set_erosion_steps(self):
        pass

    def set_dilation_steps(self):
        pass

    def set_target_area(self):
        pass

    def set_target_fullness(self):
        pass

    def set_target_aspect_ration(self):   
        pass    

    def set_target_region(self):
        pass

    def set_source_image(self):
        pass

    def set_crosshair_mode(self):
        pass

    def set_crosshair_type(self):
        pass     

    def clampHSV(self, hsv_value):
        if hsv_value[0]<0: hsv_value[0] = 0
        if hsv_value[1]>255: hsv_value[1] = 255
    