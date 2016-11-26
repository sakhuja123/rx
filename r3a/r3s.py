import RPi.GPIO as GPIO
import time

def get_dist(self, sensorid = 'zz'):
    GPIO.setmode(GPIO.BCM)
    TRIG=23
    ECHO = get_sensorpin(sensorid)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup (ECHO,GPIO.IN)

    GPIO.output(TRIG,False)
    time.sleep(0.3)
    GPIO.output(TRIG,True)
    time.sleep (0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        ps=time.time()

    while GPIO.input(ECHO)==1:
        pe=time.time()

    #print "got start and end times, calculating distance now"
    pd = pe - ps
    distance=pd*17150/2
    distance=round(distance,2)
    print ">> Sensor ID: ",sensorid,":",ECHO," Dist: ",distance,"cm"

    GPIO.cleanup()
    return distance

def get_sensorpin(self, sensorid = 'xx'):
    print "@Sensor ID: ",sensorid
    return {
        'fl': 00,
        'fc': 24, 
        'fr': 11,
        'rl': 00,
        'rc': 00,
        'rr': 00,
        'fdl': 00,
        'fdr': 00,
    }.get(sensorid, 99)
