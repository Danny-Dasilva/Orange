import cv2
from threading import Thread
import numpy as np
from time import sleep
import enum
import math
import threading

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
    def __init__(self, qu):
        self.qu = qu
        self.img = None
        self.exposure = 157 #ms #ON CORAL
        self.white_balance = 100 #CHANGE #ON CORAL
        self.hue = (20, 255) #Pixel
        self.saturation = (20,255) #Pixel
        self.value = (40,255) #Pixel
        self.erosion = 0 #CHANGE
        self.dilation = 0 #CHANGE
        self.target_area = 4000
        self.target_fullness = 0
        self.target_aspect_ratio = 1
        self.target_region = targetRegion.center
        self.eyedropper_mode = "max"
        self.crosshair_mode = None #CHANGE
        self.crosshair_type = None #CHANGE
        self._process= threading.Thread(target=self._process)
        self.start()
    def put(self, tensor):
        
        self.img = tensor.reshape(480, 640, 3)
        print(tensor.shape)
        
        
        

    def _process(self):
        print("started")
        counter = 0
        sleep(3)
        while True:
            print("1")
            sleep(.03)
            counter +=1
            self.qu.put(counter)
            img = self.img
            #print(img.shape, "img")
            ## convert to hsv
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            #print(hsv.shape, "hsv")
            mask = cv2.inRange(hsv, (int(self.hue[0]), int(self.saturation[0]), int(self.value[0])), (int(self.hue[1]), int(self.saturation[1]),int(self.value[1])))
            #print(mask.shape, "shape")
            image, contours, hierarchy= cv2.findContours(mask, 1, 2)
            # print(len(contours), len(hierarchy))
            colorMask = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
            boxes = []
            
            for cnt in contours:
                
                blankImg = np.zeros_like(mask)
                pixels = []
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                if cv2.contourArea(box) > self.target_area:
                    cv2.drawContours(blankImg, [box], 0, color=255, thickness=-1)
                    pixelpoints = np.nonzero(blankImg)
                    pixel_area = len(pixelpoints[0])
                    pixels.append(mask[pixelpoints[0],pixelpoints[1]])
                    mask_area = len(np.nonzero(pixels[0])[0])
                    fullness = mask_area/pixel_area
                    if fullness*100 >= self.target_fullness:
                        dist1 = math.sqrt( ((box[0][0]-box[1][0])**2)+((box[0][1]-box[1][1])**2) )
                        dist2 = math.sqrt( ((box[1][0]-box[2][0])**2)+((box[1][1]-box[2][1])**2) )
                        if dist1/dist2 > self.target_aspect_ratio:
                            pass
            #                 self.qu.put(box)
                     
            
    def start(self):
        self._process.start()

    def set_exposure(self,exposure):
        self.exposure = exposure
    
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

    def set_erosion_steps(self, erosion):
        self.erosion = erosion

    def set_dilation_steps(self,dilation):
        self.dilation = dilation

    def set_target_area(self, area):
        self.target_area = area

    def set_target_fullness(self, fullness):
        self.target_fullness = fullness

    def set_target_aspect_ration(self, target_aspect_ratio):   
        self.target_aspect_ratio = target_aspect_ratio 

    def set_target_region(self, target_region):
        self.target_region = target_region #0-8 see enum

    def set_crosshair_mode(self, crosshair_mode):
        self.crosshair_mode = crosshair_mode

    def set_crosshair_type(self, crosshair_type):
        self.crosshair_type = crosshair_type

    def clampHSV(self, hsv_value):
        if hsv_value[0]<0: hsv_value[0] = 0
        if hsv_value[1]>255: hsv_value[1] = 255
    