from drive import keybourd as kp
from djitellopy import tello
from time import sleep

kp.init()

yelo = tello.Tello()
yelo.connect()
print(yelo.get_battery())


def getKeyInput():
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = -speed
    elif kp.getKey("s"): ud = speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed



    if kp.getKey("q"): yelo.land()
    if kp.getKey("e"): yelo.takeoff()

    return [lr, fb, up, yv]


while True:
    vals = getKeyInput()
    yelo.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)