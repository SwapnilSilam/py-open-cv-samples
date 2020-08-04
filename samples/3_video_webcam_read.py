# if you face issue like `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback'
# then before running this script please run this command in cmd 'setx OPENCV_VIDEOIO_PRIORITY_MSMF 0'

import cv2

capture = cv2.VideoCapture(0)

while (True):
    result, frame = capture.read()

    print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

