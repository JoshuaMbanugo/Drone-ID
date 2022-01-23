from djitellopy import tello
from time import sleep
import  cv2

drone = tello.Tello()
drone.connect()
x=1



drone.streamon()
while(x == 1):
    img = drone.get_frame_read().frame
    #img = cv2.resize(img, (360, 360))
    cv2.imshow("image", img)
    cv2.waitKey(1)

print(drone.get_battery())

print("Take off")
drone.takeoff()
drone.send_rc_control(0,0,0,30)
print(drone.get_height())
sleep(0.5)
print("Droping----------------------------------------")
drone.land()
print(drone.get_height())

x = 0
