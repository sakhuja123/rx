import RPi.GPIO as GPIO
import time
import math
import string

GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=24

print "distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup (ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print "waiting for sensors"
time.sleep(2)
print "trigger pulse start"
GPIO.output(TRIG,True)
time.sleep (0.00001)
GPIO.output(TRIG,False)
print "trigger pulse stop"
print "getting echo start time"
while GPIO.input(ECHO)==0:
    #print "echo value==0"
    pulse_start=time.time()
print "ECHO value is"+ str(ECHO)
print "getting echo end time"
while GPIO.input(ECHO)==1:
    print "echo value==1"
    pulse_end=time.time()

print "got start and end times, calculating distance now"
pulse_duration = pulse_end - pulse_start
distance=pulse_duration*17150
distance=round(distance,2)
print "distance: ",distance,"cm"


GPIO.cleanup()

