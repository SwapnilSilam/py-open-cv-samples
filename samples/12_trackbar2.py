import numpy as np
import cv2 as cv


def evnet_catch(x):
    print(x)


#creating namded window
cv.namedWindow("Image")

switch = 'color/gray'
cv.createTrackbar("CurrentPostion", "Image", 0, 255, evnet_catch)
cv.createTrackbar(switch, "Image", 0, 1, evnet_catch)

while (1):
    img = cv.imread('lena.jpg')

    cp = cv.getTrackbarPos("CurrentPostion", "Image")
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(cp), (50, 100), font, 1, (0, 0, 255), 5)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv.getTrackbarPos(switch, "Image")
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    cv.imshow("Image", img)

cv.destroyAllWindows()