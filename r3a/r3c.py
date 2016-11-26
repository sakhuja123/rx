import sys
import time
import datetime
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT
from r3s import get_dist

class r3c(object):
    def __init__(self, addr=0x60, left_front_id=1, right_front_id=2,left_rear_id=3, right_rear_id=4, left_trim=0, right_trim=0,
                 stop_at_exit=True):

                 define_vars()

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

    def nav(self, left_speed, right_speed, run_duration=5):
        move_command = get_move_command(left_speed, right_speed)
        run_start_time = time.time()
        while((time.time() - run_start_time) <= run_duration):
            self.move(left_speed, right_speed)
            print "navigating: all good.. "
            if(get_dist('fc') < 5 and (('FWD' in move_command) or ('PIVOT' in move_command))):
                print "obstacle!"
                self.pause()
                self.nav(-80,-80,2)
                self.pivot(5)
        self.stop()
        print "run time up!"

    def get_move_command(self, left_speed, right_speed):
        move_command = 'UNKNOWN'
        if(left_speed > 0 and right_speed > 0):
            if(left_speed == right_speed):
                move_command = 'FWD'
            if(left_speed > right_speed):
                move_command = 'FWD_RIGHT'
            if(left_speed < right_speed):
                move_command = 'FWD_LEFT'
        elif(left_speed < 0 and right_speed < 0):
            move_command = 'RVRS'
            #@TODO: add RVRS left and right commands
        elif(left_speed == 0 and right_speed > 0):
            move_command = 'PIVOT_LEFT'
        elif(left_speed > 0 and right_speed < 0):
            move_command = 'PIVOT_RIGHT'
        elif(left_speed == 0 and right_speed == 0):
            move_command = 'PAUSE'
        return move_command

    def pivot(self,side='left',run_duration=5):
        if(side=='left'):
            print "pivot left"
            self.nav(255,-255,run_duration)
        if(side=='right'):
            print "pivot right"
            self.nav(-255,255,run_duration)

    def pause(self, max_pause_duration=20):
        self.move(0, 0)

    def stop(self):
        """Stop all movement."""
        self._left_front.run(Adafruit_MotorHAT.RELEASE)
        self._right_front.run(Adafruit_MotorHAT.RELEASE)
        self._left_rear.run(Adafruit_MotorHAT.RELEASE)
        self._right_rear.run(Adafruit_MotorHAT.RELEASE)
        print "stopped"

    def move(self, left_speed=65, right_speed=65):
        self._set_speed(left_speed, 'left')
        self._set_speed(right_speed, 'right')

        if(left_speed >= 0):
            self._left_front.run(Adafruit_MotorHAT.FORWARD)
            self._left_rear.run(Adafruit_MotorHAT.FORWARD)
        else:
            self._left_front.run(Adafruit_MotorHAT.BACKWARD)
            self._left_rear.run(Adafruit_MotorHAT.BACKWARD)

        if(right_speed >= 0):
            self._right_front.run(Adafruit_MotorHAT.FORWARD)
            self._right_rear.run(Adafruit_MotorHAT.FORWARD)
        else:
            self._right_front.run(Adafruit_MotorHAT.BACKWARD)
            self._right_rear.run(Adafruit_MotorHAT.BACKWARD)

    def _set_speed(self, speed, side='both'):
        assert -255 <= speed <= 255, 'Speed must be a value between -255 to 255 inclusive!'

        if(side == 'left' or side == 'both'):
            speed += self._left_trim
            speed = max(-255, min(255, speed))
            self._left_front.setSpeed(abs(speed))
            self._left_rear.setSpeed(abs(speed))
        elif(side=='right' or side == 'both'):
            speed += self._right_trim
            speed = max(-255, min(255, speed))
            self._right_front.setSpeed(abs(speed))
            self._right_rear.setSpeed(abs(speed))

    def define_vars(self):
        global move_command
        move_command = 'NONE'    

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

    def _left_speedxx(self, speed):
        """Set the speed of the left motor, taking into account its trim offset.
        """
        #assert 0 <= speed <= 255, 'Speed must be a value between 0 to 255 inclusive!'
        assert -255 <= speed <= 255, 'Speed must be a value between 0 to 255 inclusive!'
        speed += self._left_trim
        #speed = max(0, min(255, speed))  # Constrain speed to 0-255 after trimming.
        speed = max(-255, min(255, speed))  # Constrain speed to 0-255 after trimming.
        self._left_front.setSpeed(abs(speed))
        self._left_rear.setSpeed(abs(speed))

    def _right_speedxx(self, speed):
        """Set the speed of the right motor, taking into account its trim offset.
        """
        assert 0 <= speed <= 255, 'Speed must be a value between 0 to 255 inclusive!'
        speed += self._right_trim
        speed = max(0, min(255, speed))  # Constrain speed to 0-255 after trimming.
        self._right_front.setSpeed(speed)
        self._right_rear.setSpeed(speed)

    def nav_working(self, left_speed, right_speed, run_duration=5):
        run_start_time = time.time()
        while((time.time() - run_start_time) <= run_duration):
            while(get_dist('fc') > 5):
                self.move(left_speed, right_speed)
                print "navigating: all good.. "
            print "obstacle!"
            self.pause()
        self.stop()
        print "run time up!"
