import numpy as np
import cv2 as cv
import os


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path


# Read image
frame = cv.imread(GetImagePath("Images", "gradient.png"), 1)

# Thresholding techiques 
_, th1 = cv.threshold(frame, 127, 255, cv.THRESH_BINARY) # Threshold binary -> if pixel less than 127 then 0 else 1
_, th2 = cv.threshold(frame, 127, 255, cv.THRESH_BINARY_INV) # Threshold binary inverse -> if pixel less than 127 then 1 else 0
_, th3 = cv.threshold(frame, 127, 255, cv.THRESH_TRUNC) # Threshold trunch -> if pixel less then 127 then 0 else 127
_, th4 = cv.threshold(frame, 127, 255, cv.THRESH_TOZERO) # Threshold zero -> if pixel less than 127 then 0 else no change in pixel values
_, th5 = cv.threshold(frame, 127, 255, cv.THRESH_TOZERO_INV) # Threshold zero invers -> if pixel greater than 127 then 0 else no changes in pixel values

# Show all images 
cv.imshow("Frame", frame)
cv.imshow("ThresHoldBinary", th1)
cv.imshow("ThresHoldBinaryInvers", th2)
cv.imshow("ThresHoldTrunc", th3)
cv.imshow("ThresHoldZero", th4)
cv.imshow("ThresHoldZeroInvers", th5)

# Wait for any input
cv.waitKey(0)

# Destroy all windows and clear memory
cv.destroyAllWindows()