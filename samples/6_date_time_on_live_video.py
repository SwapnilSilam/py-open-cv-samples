import cv2
import datetime

capture = cv2.VideoCapture(0)

while (capture.isOpened()):
    result, frame = capture.read()

    if result == True:
        text = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX

        frame = cv2.putText(frame, text, (10, 25), font, 1, (0, 255, 255), 1,
                            cv2.LINE_AA)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()