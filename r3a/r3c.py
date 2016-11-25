import sys
import time
import datetime
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT
from r3s import get_dist

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

    def nav(self, left_speed=50, right_speed=50, run_duration=2):
        self._left_speed(left_speed)
        self._right_speed(right_speed)

        self._left_front.run(Adafruit_MotorHAT.FORWARD)
        self._right_front.run(Adafruit_MotorHAT.FORWARD)
        self._left_rear.run(Adafruit_MotorHAT.FORWARD)
        self._right_rear.run(Adafruit_MotorHAT.FORWARD)

        run_start_time = time.time()
        current_time = time.time()
        print "run stats:"
        print run_duration
        print run_start_time
        print current_time
        while((current_time - run_start_time) <= run_duration):
            while(get_dist('fc') > 15):
                    #time.sleep(duration)
                    print time.time(), "all good.. keep it movin' "
            self.pause()
            print "obstacle, waiting!"
            current_time = time.time()
        self.stop()
        print "time up! stopping"

    def pause(self, left_speed=0, right_speed=0, max_pause_duration=20):
        self._left_speed(left_speed)
        self._right_speed(right_speed)

        self._left_front.run(Adafruit_MotorHAT.FORWARD)
        self._right_front.run(Adafruit_MotorHAT.FORWARD)
        self._left_rear.run(Adafruit_MotorHAT.FORWARD)
        self._right_rear.run(Adafruit_MotorHAT.FORWARD)

        time.sleep(max_pause_duration)
        self.stop()
        print "stopping! was paused too long :("


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

    def stop(self):
        """Stop all movement."""
        self._left_front.run(Adafruit_MotorHAT.RELEASE)
        self._right_front.run(Adafruit_MotorHAT.RELEASE)
        self._left_rear.run(Adafruit_MotorHAT.RELEASE)
        self._right_rear.run(Adafruit_MotorHAT.RELEASE)


######################################################################
######################################################################
######################################################################
######################################################################

    def move_old(self, left_speed=50, right_speed=50, duration=3):
        self._left_speed(left_speed)
        self._right_speed(right_speed)

        self._left_front.run(Adafruit_MotorHAT.FORWARD)
        self._right_front.run(Adafruit_MotorHAT.FORWARD)
        self._left_rear.run(Adafruit_MotorHAT.FORWARD)
        self._right_rear.run(Adafruit_MotorHAT.FORWARD)
        if duration is not None:
            time.sleep(duration)
            self.stop()

    def nav2(self, left_speed=50, right_speed=50, duration=20):
    #nav takes into account obstacle avoidance while
    #def r3_nav(self, 100, 100, 30):
        print "nav2 start"
        self.move(left_speed, right_speed, duration)
        while(get_dist('fc') > 20):
            #time.sleep(.5)
            print "all good.. going fwd"
        print "something in the way"
        self.stop()
        print "nav2 stop"

    def nav_deprecated(self, left_speed=50, right_speed=50, duration=20):
    #nav takes into account obstacle avoidance while
    #def r3_nav(self, 100, 100, 30):
        i = 0
        print "nav start"
        print 'move steps: ',(duration )
        for i in range(0, (duration)):
            while(get_dist('fc') > 20):
                 self.move(left_speed, right_speed, 1)
                 #print "move call from nav"
                 i = i + 1
                 #print "i is:",i
                 #print "dist: ",get_dist('fc')
        self.stop()
        print "nav stop"
