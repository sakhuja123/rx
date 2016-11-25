import RPi.GPIO as GPIO
import time

def get_sensor_pin(self, sensorid = 'fc'):
    return {
        'fl': 24,
        'fc': 24,
        'fr': 24,
        'rl': 24,
        'fc': 24,
        'rr': 24,
        'fdc': 24,
        'fdr': 24,
    }.get(sensorid, 24)

def get_dist(self, sensorid = 'fc'):
    GPIO.setmode(GPIO.BCM)
    TRIG=23
    ECHO = self.get_sensor_pin(sensorid)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup (ECHO,GPIO.IN)

    GPIO.output(TRIG,False)
    time.sleep(0.1)
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
    print ">> Sensor ID: ",sensorid,"-",ECHO," Dist: ",distance," cm"

    GPIO.cleanup()
    return distance

def get_dist_old(sensorid = 'fc', measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(16, gpio.OUT)
    gpio.setup(18, gpio.IN)

    time.sleep(0.3)
    gpio.output(16, True)
    time.sleep(0.00001)

    gpio.output(16, False)
    while gpio.input(18) == 0:
        nosig = time.time()

    while gpio.input(18) == 1:
        sig = time.time()

    tl = sig - nosig

    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('Improper choice of measurement: in or cm')
        distance = None

    gpio.cleanup()
    return distance

#print(distance('cm'))
