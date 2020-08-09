import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path


# Read image
img = cv.imread(GetImagePath("Images", "messi5.jpg"), cv.IMREAD_GRAYSCALE)

# Laplacian method to edge detection

laplacian = cv.Laplacian(img, cv.CV_64F, ksize=3)
laplacian = np.uint8(np.absolute(laplacian))

# Sobel X method to edge detection
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

# Sobel Y method to edge detection
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

# BitWise OR =>  Sobel X || Soble Y
sobelXorY = cv.bitwise_or(sobelX, sobelY)

# Sobel XY method to edge detection
sobelXY = cv.Sobel(img, cv.CV_64F, 2, 2)
sobelXY = np.uint8(np.absolute(sobelXY))

# Canny edge detection
canny = cv.Canny(img, 100, 200)

# Titles array
titles = ['Original Image', 'laplacian',
          "sobelX", "sobelY", "sobelXorY", "sobelXY", "canny"]

# Images array
images = [img, laplacian, sobelX, sobelY, sobelXorY, sobelXY, canny]

# Loop through the arrays and arrange a images in 2X3 matrix format
for i in range(7):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray'),
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

# Show all images
plt.show()

# Wait for any input
cv.waitKey(0)

# Destroy all windows and clear memory
cv.destroyAllWindows()
