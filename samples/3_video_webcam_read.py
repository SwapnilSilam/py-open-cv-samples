# if you face issue like `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback'
# then before running this script please run this command in cmd 'setx OPENCV_VIDEOIO_PRIORITY_MSMF 0'

import cv2

# Get PC/Laptop's default web cam if you have more than 1 web cams then you need to find you device id
capture = cv2.VideoCapture(0)

# While is used for getting frame ( means : Image) from web cam and showing continuesly and it's shown as video
while (True):
    # Read frame / Image from WebCam
    result, frame = capture.read()

    # Printing Frames propeties 
    print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Conveting frame color to gray
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Show image
    cv2.imshow("Frame", gray)

    # Wait for user input and by pressing 'q' end program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release PC/Laptop webcam resources 
capture.release()

# Distroy all windows and release memory
cv2.destroyAllWindows()

