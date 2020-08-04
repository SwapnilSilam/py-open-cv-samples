import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path


# Read image
frame = cv.imread(GetImagePath("Images", "gradient.png"), 1)

# Thresholding techiques
_, th1 = cv.threshold(
    frame, 127, 255, cv.THRESH_BINARY
)  # Threshold binary -> if pixel less than 127 then 0 else 1
_, th2 = cv.threshold(
    frame, 127, 255, cv.THRESH_BINARY_INV
)  # Threshold binary inverse -> if pixel less than 127 then 1 else 0
_, th3 = cv.threshold(
    frame, 127, 255, cv.THRESH_TRUNC
)  # Threshold trunch -> if pixel less then 127 then 0 else 127
_, th4 = cv.threshold(
    frame, 127, 255, cv.THRESH_TOZERO
)  # Threshold zero -> if pixel less than 127 then 0 else no change in pixel values
_, th5 = cv.threshold(
    frame, 127, 255, cv.THRESH_TOZERO_INV
)  # Threshold zero invers -> if pixel greater than 127 then 0 else no changes in pixel values

# Titles array
titles = [
    'Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV'
]

# Images array
images = [frame, th1, th2, th3, th4, th5]

# Loop through the arrays and arrange a images in 2X3 matrix format
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray'),
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

# Show all images
plt.show()

# Wait for any input
cv.waitKey(0)

# Destroy all windows and clear memory
cv.destroyAllWindows()