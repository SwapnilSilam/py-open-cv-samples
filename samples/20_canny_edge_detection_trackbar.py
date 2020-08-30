import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path

# Empty do nothig function for trackers
def nothing(x):
    pass

# Named window for showing trackers
named_window = "Trackers"
cv.namedWindow(named_window)

# Lower X and Y value tracker
cv.createTrackbar("X", named_window, 0, 300, nothing)
cv.createTrackbar("Y", named_window, 0, 300, nothing)

while True :
    # Read image
    img = cv.imread(GetImagePath("Images", "messi5.jpg"), cv.IMREAD_GRAYSCALE)

    X = cv.getTrackbarPos("X", named_window)
    Y = cv.getTrackbarPos("Y", named_window)

    # Canny Edge dection :
    # Canny edge dection perform following 5 steps
    # 1. Noise reduction
    # 2. Gradiant calculation
    # 3. Non-maximum supression 
    # 4. Double threshold 
    # 5. Edge tracking by Hysteresis
    canny = cv.Canny(img, X, Y)

    # Show all images 
    cv.imshow("OutputFrame", canny)

    # Loop breaks by pressing esc
    key = cv.waitKey(1)
    if key == 27:
        break

# Destroy all windows which are created and clear memory
cv.destroyAllWindows()