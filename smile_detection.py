import cv2
import numpy as np
import sys

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

sF = 1.05

while True:

    ret, frame = cap.read() # Capture frame-by-frame
    img = frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,scaleFactor= sF,minNeighbors=8,minSize=(55, 55),flags=cv2.CASCADE_SCALE_IMAGE)
    # ---- Draw a rectangle around the faces

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smile = smileCascade.detectMultiScale(roi_gray,scaleFactor= 1.7,minNeighbors=22,minSize=(25, 25),flags=cv2.CASCADE_SCALE_IMAGE)

        # Set region of interest for smiles
        for (x, y, w, h) in smile:
            print ("Found smiles!")
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
            #print "!!!!!!!!!!!!!!!!!"

    #cv2.cv.Flip(frame, None, 1)
    #cv2.imshow('Smile Detector', frame)
    k = cv2.waitKey(33)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
