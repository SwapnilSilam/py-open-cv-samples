import numpy as np
import cv2 as cv
import os


# Get absolute path of given image name
def GetImagePath(folderName, imageName):
    absolute_path = os.path.join(os.getcwd(), folderName, imageName)
    return absolute_path


# Read Video
cap = cv.VideoCapture(GetImagePath("Videos", "vtest.avi"))

# Read first two frames from video
_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    # Difference of two frames
    difference = cv.absdiff(frame1, frame2)
    # Convert image into gray scale ( As we know in gray scale image we will get good contours as compared to colored image)
    gray = cv.cvtColor(difference, cv.COLOR_BGR2GRAY)
    # Blur the image using gaussian blus techique
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    # Get throshold image
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    # Dilated image
    dilated = cv.dilate(thresh, None, iterations=3)
    # Find countours from dilated image
    contours, _ = cv.findContours(
        dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Draw contours on frame 1
    # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # Instead of drawing contoursm, let's draw rectangle around moving object
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)

        # If contour is area less than 900 then don't draw rectangle
        if cv.contourArea(contour) < 900:
            continue

        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv.putText(frame1, "Status : Movement", (10, 20),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show image
    cv.imshow("Motion dection", frame1)

    # Update frames
    frame1 = frame2
    _, frame2 = cap.read()

    if cv.waitKey(40) == 27:
        break

# Release video object
cap.release()

# Destroy all windows and release all used memory
cv.destroyAllWindows()
