import numpy as np
import cv2 as cv
import os


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path


# Read image
img = cv.imread(GetImagePath("Images", "shapes.jpg"))

# Converting image into grayscale image
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Get threshold image
ret, threshold = cv.threshold(img_gray, 240, 255, 0)

# Get contours
contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    # Find Ploy points using contour
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)

    # Draw contour
    cv.drawContours(img, [approx], 0, (0, 0, 0), 5)

    # Find X and Y point for put text at that location
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    # Based on length of approx decide shape
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
    elif len(approx) == 4:
        rectx, recty, rectw, recth = cv.boundingRect(approx)

        aspectRatio = float(rectw)/recth
        print(aspectRatio)

        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(img, "Square", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
        else:
            cv.putText(img, "rectangle", (x, y),
                       cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
    elif len(approx) == 5:
        cv.putText(img, "Pentagon", (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
    elif len(approx) == 10:
        cv.putText(img, "Star", (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
    else:
        cv.putText(img, "Circle", (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)


# Show Images
cv.imshow("Image", img)

# Wait for any input
cv.waitKey(0)

# Destroy all windows and clear memory
cv.destroyAllWindows()
