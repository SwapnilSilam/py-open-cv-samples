import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path


# Read image
img = cv.imread(GetImagePath("Images", "lena.jpg"))
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Define kernal for fileter 2D
kernal = np.ones(
    (5, 5), np.float32) / 25  # Formula  = 1/(width X hight) X [5 X 5]

# Smoothing image
filter2d = cv.filter2D(img, -1, kernal)
blur = cv.blur(img, (5, 5))
gaussianBlur = cv.GaussianBlur(img, (5, 5), 0)
medianFilter = cv.medianBlur(img, 5)
bilitralFilter = cv.bilateralFilter(img, 9, 99, 99)

# Titles array
titles = ['Original Image', 'Filter2d', 'Blur', 'GaussianBlur', 'MedianFilter', 'BilitralFilter']

# Images array
images = [img, filter2d, blur, gaussianBlur, medianFilter, bilitralFilter]

# Loop through the arrays and arrange a images in 2X3 matrix format
for i in range(6):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray'),
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

# Show all images
plt.show()

# Wait for any input
cv.waitKey(0)

# Destroy all windows and clear memory
cv.destroyAllWindows()