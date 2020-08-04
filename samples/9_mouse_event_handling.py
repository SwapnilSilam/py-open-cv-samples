import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow("Frame", img)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue = img[y, x, 0]
        green = img[y, x, 2]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow("Frame", img)
    if event == cv2.EVENT_MOUSEMOVE:
        print(x, ',', y)


img = cv2.imread('lena.jpg', 1)
cv2.imshow("Frame", img)

cv2.setMouseCallback("Frame", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()