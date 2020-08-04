import numpy as np
import cv2 as cv
import os


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path

# Read image
frame = cv.imread(GetImagePath("Images", "sudoku.png"), 0)

# Apply normal thresholding ( Global )
_, thGlobal = cv.threshold(frame, 127, 255, cv.THRESH_BINARY)

# Apply Adaptive thresholding (Perticular block )
thMeanC = cv.adaptiveThreshold(frame, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                  cv.THRESH_BINARY, 21, 3)
thGaussian = cv.adaptiveThreshold(frame, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv.THRESH_BINARY, 21, 3)

# Show output images
cv.imshow("Frame", frame)
cv.imshow("Global Threshold", thGlobal)
cv.imshow("Mean C Threshold", thMeanC)
cv.imshow("Gaussian Threshold", thGaussian)

# Wait for perticular key press
cv.waitKey(0)

# Destroy all open windows and clear memory
cv.destroyAllWindows()
