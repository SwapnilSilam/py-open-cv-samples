import numpy as np
import cv2
import os

# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path

# Read image
img = cv2.imread(GetImagePath("Images", "lena.jpg"), 1)

# Show image
cv2.imshow("Lena Image", img)

# Wait for input from user
key = cv2.waitKey(0)

# End program using ESC key
if key == 27 :
    cv2.destroyAllWindows() # Distroy all windows and release memory 
elif key == ord('s') :  # Create copy of image by pressing 's'
    cv2.imwrite("lena_copy.png", img)  # Write on image
    cv2.destroyAllWindows() # Distroy all windows and release memory
