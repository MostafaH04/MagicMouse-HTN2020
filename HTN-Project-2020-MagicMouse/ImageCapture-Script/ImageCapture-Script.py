#Importing openCV, OS, time, and numpy libraries
import cv2
import os
import time
import numpy as np

#Defining variables for number of saved images
count = 0
saveCount = 0


#Defines the path for the folders
imgPath = 'E:\HTN-Project\ImageCapture-Script\Info\pictures'

#Creats the folder to save the images too
global fileCount
fileCount = 0
while os.path.exists(imgPath + str(fileCount)):
    fileCount += 1
os.makedirs(imgPath + str(fileCount))

video = cv2.VideoCapture(0)

while video.isOpened():
    ret, img = video.read()
    keyPressed = cv2.waitKey(1)

    if count % 1 == 0:
        currentTime = time.time()
        cv2.imwrite(imgPath + str(fileCount)+ '/' + str(saveCount) + " "+ str(currentTime) + ".png", img)
        saveCount += 1
    count += 1

    cv2.imshow("VideoCapture", img)

    if keyPressed == ord('q'):
        break

cap.release()
cap.destroyAllWindows()


 