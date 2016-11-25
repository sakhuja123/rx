import sys
import time
import time
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT
from r3_sensor_dist import get_dist


class r3c(object):
    def __init__(self, addr=0x60, left_front_id=1, right_front_id=2,left_rear_id=3, right_rear_id=4, left_trim=0, right_trim=0,
                 stop_at_exit=True):
                # Initialize motor HAT and left, right motor.
                self._mh = Adafruit_MotorHAT(addr)
                self._left_front = self._mh.getMotor(left_front_id)
                self._right_front = self._mh.getMotor(right_front_id)
                self._left_rear = self._mh.getMotor(left_rear_id)
                self._right_rear = self._mh.getMotor(right_rear_id)
                self._left_trim = left_trim
                self._right_trim = right_trim
                # Start with motors turned off.
                self._left_front.run(Adafruit_MotorHAT.RELEASE)
                self._right_front.run(Adafruit_MotorHAT.RELEASE)
                self._left_rear.run(Adafruit_MotorHAT.RELEASE)
                self._right_rear.run(Adafruit_MotorHAT.RELEASE)
               # Configure all motors to stop at program exit if desired.
                if stop_at_exit:
                    atexit.register(self.stop)

    def _left_speed(self, speed):
        """Set the speed of the left motor, taking into account its trim offset.
        """
        assert 0 <= speed <= 255, 'Speed must be a value between 0 to 255 inclusive!'
        speed += self._left_trim
        speed = max(0, min(255, speed))  # Constrain speed to 0-255 after trimming.
        self._left_front.setSpeed(speed)
        self._left_rear.setSpeed(speed)

    def _right_speed(self, speed):
        """Set the speed of the right motor, taking into account its trim offset.
        """
        assert 0 <= speed <= 255, 'Speed must be a value between 0 to 255 inclusive!'
        speed += self._right_trim
        speed = max(0, min(255, speed))  # Constrain speed to 0-255 after trimming.
        self._right_front.setSpeed(speed)
        self._right_rear.setSpeed(speed)

    def move(self, left_speed=100, right_speed=100, duration=3):
    #def r3_move(self, -100, 255, 20):
        self._left_speed(left_speed)
        self._right_speed(right_speed)

        self._left_front.run(Adafruit_MotorHAT.FORWARD)
        self._right_front.run(Adafruit_MotorHAT.BACKWARD)
        self._left_rear.run(Adafruit_MotorHAT.FORWARD)
        self._right_rear.run(Adafruit_MotorHAT.BACKWARD)
        if duration is not None:
            time.sleep(duration)
            self.stop()

    def nav(self, left_speed, right_speed, duration):
    #nav takes into account obstacle avoidance while
    #def r3_nav(self, 100, 100, 30):
        i = 0
        while (i < (duration/0.25)):
            move(self, left_speed, right_speed, 0.25)
            i = i+0.25
            if(r3.get_dist('fc') < 50):
                 i = duration +1 #to exit the nav mode

    def stop(self):
        """Stop all movement."""
        self._left_front.run(Adafruit_MotorHAT.RELEASE)
        self._right_front.run(Adafruit_MotorHAT.RELEASE)
        self._left_rear.run(Adafruit_MotorHAT.RELEASE)
        self._right_rear.run(Adafruit_MotorHAT.RELEASE)
