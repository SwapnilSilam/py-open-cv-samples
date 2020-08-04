import numpy as np
import cv2

img = cv2.imread("lena.jpg", 1)

# draw line on image
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

# draw arrow on image
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5)

# draw squere on image
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 5)

# draw circel on image
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

# Put text on image
img = cv2.putText(img, "OpenCV", (10, 500), cv2.QT_FONT_BLACK, 4,
                  (0, 255, 255), 5, cv2.LINE_8)

#drwa polylines

# Polygon corner points coordinates 
pts = np.array([[25, 70], [25, 160],  
                [110, 200], [200, 160],  
                [200, 70], [110, 20]], 
               np.int32) 

print(pts)
pts = pts.reshape((-1, 1, 2)) 

print(pts)
img = cv2.polylines(img, [pts], True, (255, 255, 255), 5)

cv2.imshow("Lena Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
