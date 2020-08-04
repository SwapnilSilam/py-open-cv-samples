import numpy as np
import cv2 as cv

# Empty do nothig function for trackers
def nothing(x):
    pass

# Capture image from your default camera
capture = cv.VideoCapture(0)

# Named window for showing trackers
named_window = "Trackers"
cv.namedWindow(named_window)

# Lower HSV value tracker
cv.createTrackbar("LH", named_window, 0, 255, nothing)
cv.createTrackbar("LS", named_window, 0, 255, nothing)
cv.createTrackbar("LV", named_window, 0, 255, nothing)

# Uppper HSV value tracker
cv.createTrackbar("UH", named_window, 255, 255, nothing)
cv.createTrackbar("US", named_window, 255, 255, nothing)
cv.createTrackbar("UV", named_window, 255, 255, nothing)

while True:
    # Read image from video
    _, frame = capture.read()

    # Read Lower HSV values from trackers
    l_h = cv.getTrackbarPos("LH", named_window)
    l_s = cv.getTrackbarPos("LS", named_window)
    l_v = cv.getTrackbarPos("LV", named_window)

    # Read upper HSV values from trackers
    u_h = cv.getTrackbarPos("UH", named_window)
    u_s = cv.getTrackbarPos("US", named_window)
    u_v = cv.getTrackbarPos("UV", named_window)

    # Using numpy array creating lower andupper boundry for color dectection from HSV color space
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # Convert loaded image into HVS image
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Create mask image for detecting colors
    mask = cv.inRange(hsv_frame, l_b, u_b)

    # Color detection using bitwise and with orignal image and mask
    output_frame = cv.bitwise_and(frame, frame, mask=mask)

    # Show all images 
    cv.imshow("Frame", frame)
    cv.imshow("MaskedFrame", mask)
    cv.imshow("OutputFrame", output_frame)

    # Loop breaks by pressing esc
    key = cv.waitKey(1)
    if key == 27:
        break

# Release default camera and clear memory
capture.release()

# Destroy all windows which are created and clear memory
cv.destroyAllWindows()
