# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:15:43 2020

@author: omarnasir
"""
import cv2
import face_recognition


all_face_locations = []
web_cam_video_stream = cv2.VideoCapture('images/pewds.mp4')

while True:
    ret, current_frame = web_cam_video_stream.read()
    
    current_frame_small = cv2.resize(current_frame,(0,0), fx=0.25, fy=0.25)
    
    all_face_locations = face_recognition.face_locations(current_frame_small,number_of_times_to_upsample = 2,model="hog")
    
    for index,current_face_location in enumerate(all_face_locations):
        top_pos,right_pos,bottom_pos,left_pos = current_face_location
        
        top_pos = top_pos * 4
        right_pos = right_pos * 4
        bottom_pos = bottom_pos * 4
        left_pos = left_pos * 4
        
        print("Found face {} at top:{},right:{},bottom:{},left:{}".format(index+1,top_pos,right_pos,bottom_pos,left_pos))
        
        current_face_image = current_frame[top_pos:bottom_pos,left_pos:right_pos]
        current_face_image = cv2.GaussianBlur(current_face_image, (99,99), 30)
        current_frame[top_pos:bottom_pos,left_pos:right_pos] = current_face_image
        cv2.rectangle(current_frame,(left_pos, top_pos), (right_pos, bottom_pos), (0, 0, 255), 2)
        
    cv2.imshow("Webcam Video", current_frame)
    
    if(cv2.waitKey(1) & 0xFF == ord('o')):
        break
    
web_cam_video_stream.release()
cv2.destroyAllWindows()
