import RPi.GPIO as GPIO
import time

def get_dist(self, sensorid = 'fc'):
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
    #print ">> Sensor ID: ",sensorid,"-",ECHO," Dist: ",distance," cm"

    GPIO.cleanup()
    return distance

def get_sensorpin(self, sensorid = 'fc'):
    return {
        'fl': 24,
        'fc': 24,
        'fr': 24,
        'rl': 24,
        'rc': 24,
        'rr': 24,
        'fdl': 24,
        'fdr': 24,
    }.get(sensorid, 24)
