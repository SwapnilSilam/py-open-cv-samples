import numpy as np
import cv2 as cv
import os


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path


# Read image
img = cv.imread(GetImagePath("Images", "opencv-logo.png"))

# Converting image into grayscale image
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Get threshold imagesss
ret, threshold = cv.threshold(img_gray, 127, 255, 0)

# Get contures (Outline/Shape) of an object fron an Image 
# Differance between Edges Vs Contours ( https://stackoverflow.com/questions/17103735/difference-between-edge-detection-and-image-contours )
# Edges are computed as points that are extrema of the image gradient in the direction of the gradient. 
# if it helps, you can think of them as the min and max points in a 1D function. 
# The point is, edge pixels are a local notion: they just point out a significant difference between neighbouring pixels.

# Contours are often obtained from edges, but they are aimed at being object contours. 
# Thus, they need to be closed curves. You can think of them as boundaries (some Image Processing algorithms & librarires call them like that). 
# When they are obtained from edges, you need to connect the edges in order to obtain a closed contour.
contours, hierarchy = cv.findContours(
    threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# Print number of countrours on Image
print("Number of contours : " + str(len(contours)))

# Drawing contours on image
cv.drawContours(img, contours, -1, (255, 127, 100), 3)

# Show Images
cv.imshow("Image", img)
cv.imshow("Image_gray", img_gray)

# Wait for any input
cv.waitKey(0)

# Destroy all windows and clear memory
cv.destroyAllWindows()
