import RPi.GPIO as GPIO
import time

def get_dist(sensorid = 'zz'):
    GPIO.setmode(GPIO.BCM)
    TRIG=23 # board: 16 Fire trig simultaneously
    #print "sensorid to convert: ",sensorid
    #ECHO = get_sensorpin(sensorid)
    ECHO = 27
    TRIG = 17
    #print "ECHO is: ",ECHO
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup (ECHO,GPIO.IN)

    time.sleep(.1)
    GPIO.output(TRIG,False)
    #time.sleep(.5)
    GPIO.output(TRIG,True)
    time.sleep (0.0003)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        ps=time.time()

    while GPIO.input(ECHO)==1:
    #if GPIO.input(ECHO)==1:
        pe=time.time()

    #print "got start and end times, calculating distance now"
    pd = pe - ps
    distance=pd*17150/2
    distance=round(distance,2)
    print "~Sensor ID: ",sensorid,":",ECHO," Dist: ",distance,"cm"
    GPIO.cleanup()

    return distance

def get_sensorpin(sensorid = 'xx'):
    #print "@Sensor ID: ",sensorid
    return {
        'fc': 12, #Board 32
        'fl': 24, #Board 18
        'fr': 25, #board 22
        'rl': 00,
        'rc': 00,
        'rr': 00,
        'fdl': 00,
        'fdr': 00,
    }.get(sensorid, 99)
