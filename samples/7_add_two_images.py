import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r= cv2.split(img)
img = cv2.merge((b,g,r))

# Region of interest
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

#Reshaping two images
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#Adding two images
#outImg = cv2.add(img, img2) # without specifying any opeque values (Weighted values)

outImg = cv2.addWeighted(img, .8, img2, 0.2, 0) # 0.8 is for img weight and 0.2 is img2 weight and 0 is gamma ( Scalar value )


cv2.imshow("Imgae", outImg)
cv2.waitKey(0)
cv2.destroyAllWindows()