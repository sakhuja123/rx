import RPi.GPIO as gpio
import time

def get_dist(sensorid = 'fc', measure='cm'):
    GPIO.setmode(GPIO.BCM)
    TRIG=23

    ECHO-FL=24
    ECHO-FR=24
    ECHO-FC=24

    ECHO-RL=24
    ECHO-RC=24
    ECHO-RR=24

    ECHO-FDL=24
    ECHO-FDR=24

    print "measuring distance"
    GPIO.setup(TRIG,GPIO.OUT)

    GPIO.setup (ECHO-FL,GPIO.IN)
    GPIO.setup (ECHO-FR,GPIO.IN)
    GPIO.setup (ECHO-FC,GPIO.IN)

    GPIO.setup (ECHO-RL,GPIO.IN)
    GPIO.setup (ECHO-RR,GPIO.IN)
    GPIO.setup (ECHO-RC,GPIO.IN)

    GPIO.setup (ECHO-FDL,GPIO.IN)
    GPIO.setup (ECHO-FDR,GPIO.IN)

    GPIO.output(TRIG,False)
    time.sleep(0.1)
    GPIO.output(TRIG,True)
    time.sleep (0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO-FC)==0:
        ps-FC=time.time()

    while GPIO.input(ECHO-FC)==1:
        pe-FC=time.time()

    #print "got start and end times, calculating distance now"
    pd-FC = pe-FC - ps-FC
    distance=pd-FC*17150/2
    distance=round(distance,2)
    print "distance: ",distance,"cm"

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
