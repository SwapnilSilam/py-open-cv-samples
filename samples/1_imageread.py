import numpy as np
import cv2
import os

# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path

# Read image
img = cv2.imread(GetImagePath("Images", "lena.jpg"), -1)

# Show imgae
cv2.imshow("Lena Image", img)

# Wait for input 
cv2.waitKey(0)

# Destroy all windows and release memmory
cv2.destroyAllWindows()
