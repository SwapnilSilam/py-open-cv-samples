import cv2

img = cv2.imread("lena.jpg", -1)

cv2.imshow("Lena Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()