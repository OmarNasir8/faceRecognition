# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:16:44 2020

@author: omarnasir
"""

import cv2
import face_recognition

image_to_detect = cv2.imread('images/crisface.jpg')

all_face_locations = face_recognition.face_locations(image_to_detect,model="hog")

print("There are this much faces: %d"%len(all_face_locations))

for index,current_face_location in enumerate(all_face_locations):
    top_pos,right_pos,bottom_pos,left_pos = current_face_location
    print("Found face {} at top:{},right:{},bottom:{},left:{}".format(index+1,top_pos,right_pos,bottom_pos,left_pos))
    cv2.rectangle(image_to_detect,(left_pos, top_pos), (right_pos, bottom_pos), (0, 0, 255), 2)

cv2.imshow("test", image_to_detect)