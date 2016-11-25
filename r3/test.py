import time
import Robot
import r3c #r3 chassis functions

LEFT_TRIM   = 0
RIGHT_TRIM  = 0

#robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
r3 = r3c.r3c()

r3.nav(50,50,1)
time.sleep(1)
r3.nav(255,255,1)
r3.stop()

'''
#robot.forward(255, 0.2)
robot.turn('left', 255, 30)
time.sleep(5)
robot.right(255, 5)
time.sleep(1)
robot.left(255, 5)
time.sleep(1)

robot.forward(60, 10)
time.sleep(1)
robot.backward(60, 10)
time.sleep(1)

robot.forward(100, 2.0)
time.sleep(1)
robot.backward(100, 2.0)
time.sleep(1)

robot.forward(255, 1.0)
time.sleep(1)
robot.backward(255, 1.0)

robot.stop()      # Stop the robot from moving.
'''
