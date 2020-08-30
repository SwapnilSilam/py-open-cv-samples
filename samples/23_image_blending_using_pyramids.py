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

# In next Program we will try to remove it.
apple_oragne = np.hstack((apple[:, :256], orange[:, 256:]))

# Genarating Gausiann pyramid layer for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# Genarating Gausiann pyramid layer for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Genatatig Laplacian pyramid layer for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

# Genatatig Laplacian pyramid layer for Orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    gaussian_expanded = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)

# Joining right and left side of each layer
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, channel = apple_lap.shape
    laplacian = np.hstack(
        (apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Reconstruction of an Image
apple_orange_reconstuction = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstuction = cv.pyrUp(apple_orange_reconstuction)
    apple_orange_reconstuction = cv.add(
        apple_orange_pyramid[i], apple_orange_reconstuction)

# Show all images
cv.imshow("Apple", apple)
cv.imshow("Orange", orange)
cv.imshow("Apple_Orange", apple_oragne)
cv.imshow("Apple_orange_reconstuction", apple_orange_reconstuction)

# Wait for any input
cv.waitKey(0)

# Destroy all windows which are created and clear memory
cv.destroyAllWindows()
