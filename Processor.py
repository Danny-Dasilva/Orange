from __future__ import division
import numpy as np
import cv2

class Processor:
    bound_val = 0
    calibration_point = [0, 0]

    def __init__(self, camera, boundary):
        self.bound_val = boundary
        self.cam = camera
        self.frame = self.cam.get_frame()


    def display_img(self):
        cv2.namedWindow('image')
        box = self.draw_cnts()

        cv2.imshow('image', self.frame)


    def set_thresh_val(val):
        global bound_val
        bound_val = val


    def draw_cnts(self):
        self.frame = self.cam.get_frame()
        image = self.frame
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

        cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) [-2]

        if len(cnts) > 0:
            area = max(cnts, key=cv2.contourArea)
            # print(get_percentage(image, cv2.findNonZero(thresh)))
            rect = cv2.minAreaRect(area)
            box = cv2.boxPoints(rect)
            box = np.int0(box)


            # get_cnt_area(box)
            # cv2.imshow('threshold', thresh)
            # print(box)
            cv2.drawContours(self.frame, [box], 0, (0, 255, 0), 2)
            return box
            # print(x,y,w,h)   
            # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    

    def get_percentage(image, pix_in_contour):
        return (pix_in_contour.size / image.size) * 100    


    def target_dist_to_center(target):
        if target is not None:
            target_coord = center_of_cnt(target)
            dist_to_center = (calibration_point[0] - target_coord[0], target_coord[1] - calibration_point[1])
            if dist_to_center is not None:
                return dist_to_center


    def center_of_cnt(box):
        if box is not None:
            mid_x = ((abs(box[2][0] - box[1][0])) / 2) + abs(box[0][0])
            mid_y = abs(box[0][1]) - (abs(box[1][1] -  box[0][1]) / 2)
            return [mid_x, mid_y]
