from djitellopy import tello
from time import sleep
import  cv2
cap = cv2.VideoCapture(0)

drone = tello.Tello()
drone.connect()

print(drone.get_battery())
drone.streamon()


ret, frame1 = cap.read()
ret, frame2 = cap.read()

ret, droneCam = drone.get_frame_read().frame

while True:
    diff = cv2.absdiff(droneCam , frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(droneCam, (x, y), (x + w, y + h), (128, 128, 128), 2)
        cv2.putText(droneCam, "Status: {}".format('Something'), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 3)

    cv2.imshow('Detection', droneCam)
    droneCam = frame2
    ret, frame2 = cap.read()

    img = drone.get_frame_read().frame
    #img = cv2.resize(img, (360, 360))
    cv2.imshow("image", img)
    cv2.waitKey(1)

    k = cv2.waitKey(10)

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()