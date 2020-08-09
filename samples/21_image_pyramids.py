import numpy as np
import cv2 as cv
import os

# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path

# Read image
img = cv.imread(GetImagePath("Images", "lena.jpg"))

# Layes need to Gaussian Pyramids
layer = img.copy()
gp = [layer]

# Creating image pyramids using Gaussian method
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow("Gaussian" + str(i), layer)

# Laplacial pyramids
layer = gp[5]
cv.imshow("Upper level Gaussian Pyramid", layer)

for i in range(5, 0, -1):
    # taking Upper level img created by gaussian pyramid
    gaussian_extended = cv.pyrUp(gp[i])
    # Subtracting upper level from very next to upper level guassian pyramid img
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow("Laplacian" + str(i), laplacian)

# Wait for any input
cv.waitKey(0)

# Destroy all windows which are created and clear memory
cv.destroyAllWindows()
