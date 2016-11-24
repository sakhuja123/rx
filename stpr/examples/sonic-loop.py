import RPi.GPIO as GPIO
import time
import math
import string

GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=24
i=1

print "measuring distance"
while (i<20):
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup (ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    #print "adding sensor wait time"
    time.sleep(.5)
    #print "trigger pulse start"
    GPIO.output(TRIG,True)
    time.sleep (0.00001)
    GPIO.output(TRIG,False)
    #print "trigger pulse stop"
    #print "getting echo start time"
    while GPIO.input(ECHO)==0:
        #print "echo value==0"
        #pass
        pulse_start=time.time()
    #print "ECHO value is"+ str(ECHO)
    #print "getting echo end time"
    while GPIO.input(ECHO)==1:
        #print "echo value==1"
        #pass
        pulse_end=time.time()

    #print "got start and end times, calculating distance now"
    pulse_duration = pulse_end - pulse_start
    distance=pulse_duration*17150/2
    distance=round(distance,2)
    print "distance: ",distance,"cm"
    #print "count: ",i
    i = i+1

GPIO.cleanup()

