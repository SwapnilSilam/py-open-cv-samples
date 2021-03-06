import numpy as np
import cv2 as cv


def evnet_catch(x):
    print(x)


img = np.zeros((300, 512, 3), np.uint8)

#creating namded window
cv.namedWindow("Image")

switch = '0 : OFF \n 1 : ON'
cv.createTrackbar("B", "Image", 0, 255, evnet_catch)
cv.createTrackbar("G", "Image", 0, 255, evnet_catch)
cv.createTrackbar("R", "Image", 0, 255, evnet_catch)
cv.createTrackbar(switch, "Image", 0, 1, evnet_catch)

while (1):
    cv.imshow("Image", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos("B", "Image")
    g = cv.getTrackbarPos("G", "Image")
    r = cv.getTrackbarPos("R", "Image")
    s = cv.getTrackbarPos(switch, "Image")

    if s == 0 :
        img[:] = 0
    else :
        img[:] = [b, g, r]

cv.destroyAllWindows()