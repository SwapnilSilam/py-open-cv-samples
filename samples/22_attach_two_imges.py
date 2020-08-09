import numpy as np
import cv2 as cv
import os

# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path

# Read images
apple = cv.imread(GetImagePath("Images", "apple.jpg"))
orange = cv.imread(GetImagePath("Images", "orange.jpg"))

# Attaching two image side by side 
# Here I am taking apple's right side and orange's left side
# After attaching two image you will see a line between two images, that you can see by your naked eyes.
# In next Program we will try to remove it.
apple_oragne = np.hstack((apple[:, :256], orange[:, 256:]))

# Show all images
cv.imshow("Apple", apple)
cv.imshow("Orange", orange)
cv.imshow("Apple_Orange", apple_oragne)

# Wait for any input
cv.waitKey(0)

# Destroy all windows which are created and clear memory
cv.destroyAllWindows()