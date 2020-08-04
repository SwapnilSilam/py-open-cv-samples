# if you face issue like `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback'
# then before running this script please run this command in cmd 'setx OPENCV_VIDEOIO_PRIORITY_MSMF 0'

import cv2

capture = cv2.VideoCapture(0)
code = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(
    "output.avi", code, 20.0,
    (640, 480))  # outputfilename, fourcc code, frame per sec, height and Width

while (True):
    result, frame = capture.read()

    if result == True:
        print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        output.write(frame) # writing file in color image

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Showing video in window in as gray image
        cv2.imshow("Frame", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()
