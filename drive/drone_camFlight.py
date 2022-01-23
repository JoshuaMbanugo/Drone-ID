from drive import keybourd as kp
from djitellopy import tello
from time import sleep
import cv2

kp.init()
yelo = tello.Tello()
yelo.connect()
print(yelo.get_battery())
yelo.streamon()


def getKeyInput():
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 100

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = -speed
    elif kp.getKey("s"): ud = speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed


    if kp.getKey("q"): yelo.land()
    if kp.getKey("e"): yelo.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'F:/drone/venv/drive/images/{time.time}.jpg')

    return [lr, fb, up, yv]


while True:
    vals = getKeyInput()
    yelo.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    img = yelo.get_frame_read().frame
    ##img = cv2.resize(img, (360, 360))
    cv2.imshow("image", img)
    cv2.waitKey(1)