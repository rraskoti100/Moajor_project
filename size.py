import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edge = cv2.Canny(blur, 40, 40)
    dilation = cv2.dilate(edge, (5,5), iterations = 2)
    erode = cv2.erode(dilation, (5,5), iterations = 2)
    cv2.imshow("area", erode)
    #cv2.imshow("img", img)
    
    contours, hierarchy = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for con in contours:
        area = cv2.contourArea(con)
        print(area)
        if area > 100:
              print(area)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
