import numpy as np
import cv2

img = np.zeros((250, 500, 3), np.uint8)
img = cv2.rectangle(img, (200, 0), (300, 100), (255, 255, 255), -1)

print(img.shape)
img2 = cv2.imread('image_1.jpg')
img2 = cv2.resize(img2, (500, 250))
print(img2.shape)

# Bitwise AND image
bitAND = cv2.bitwise_and(img, img2)
bitOR = cv2.bitwise_or(img, img2)
bitXOR = cv2.bitwise_xor(img, img2)
bitNOTImg = cv2.bitwise_not(img)
bitNOTImg2 = cv2.bitwise_not(img2)

cv2.imshow("Image 1", img)
cv2.imshow("Image 2", img2)
cv2.imshow("Bitwise AND", bitAND)
cv2.imshow("Bitwise OR", bitOR)
cv2.imshow("Bitwise XOR", bitXOR)
cv2.imshow("Bitwise NOT IMG 1", bitNOTImg)
cv2.imshow("Bitwise NOT IMG 2", bitNOTImg2)

cv2.waitKey(0)
cv2.destroyAllWindows()
