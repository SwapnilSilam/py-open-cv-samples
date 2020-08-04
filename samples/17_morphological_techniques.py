import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path


# Read image
frame = cv.imread(GetImagePath("Images", "smarties.png"), cv.IMREAD_GRAYSCALE)

# Create masked image
_, mask = cv.threshold(frame, 220, 225, cv.THRESH_BINARY_INV)

# Define kernal ( This is squre which applied on image)
kernal = np.ones((2, 2), np.uint8)

# Morphological Transformations
dialation = cv.dilate(mask, kernal, iterations=2)
erosion = cv.erode(mask, kernal, iterations=2)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)
tophat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)
blackhat = cv.morphologyEx(mask, cv.MORPH_BLACKHAT, kernal)
cross = cv.morphologyEx(mask, cv.MORPH_CROSS, kernal)
ellipse = cv.morphologyEx(mask, cv.MORPH_ELLIPSE, kernal)
hitmiss = cv.morphologyEx(mask, cv.MORPH_HITMISS, kernal)
rect = cv.morphologyEx(mask, cv.MORPH_RECT, kernal)

# Titles array
titles = [
    'Original Image', 'Maks', 'Dialation', 'Erosion', 'Opening', 'Closing',
    'Gradient', 'TopHat', 'BalckHat', 'Cross', 'Ellipse', 'HitMiss', 'Rect'
]

# Images array
images = [
    frame, mask, dialation, erosion, opening, closing, gradient, tophat,
    blackhat, cross, ellipse, hitmiss, rect
]

# Loop through the arrays and arrange a images in 2X3 matrix format
for i in range(13):
    plt.subplot(4, 4, i + 1), plt.imshow(images[i], 'gray'),
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

# Show all images
plt.show()

# Wait for any input
cv.waitKey(0)

# Destroy all windows and clear memory
cv.destroyAllWindows()