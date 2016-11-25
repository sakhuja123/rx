import RPi.GPIO as GPIO
import time

def get_dist(sensorid = 'fc', measure='cm'):
    GPIO.setmode(GPIO.BCM)
    TRIG=23

    ECHO_FL=24
    ECHO_FR=24
    ECHO_FC=24

    ECHO_RL=24
    ECHO_RC=24
    ECHO_RR=24

    ECHO_FDL=24
    ECHO_FDR=24

    print "measuring distance"
    GPIO.setup(TRIG,GPIO.OUT)

    #GPIO.setup (ECHO-FL,GPIO.IN)
    #GPIO.setup (ECHO-FR,GPIO.IN)
    GPIO.setup (ECHO_FC,GPIO.IN)

    #GPIO.setup (ECHO-RL,GPIO.IN)
    #GPIO.setup (ECHO-RR,GPIO.IN)
    #GPIO.setup (ECHO-RC,GPIO.IN)

    #GPIO.setup (ECHO-FDL,GPIO.IN)
    #GPIO.setup (ECHO-FDR,GPIO.IN)

    GPIO.output(TRIG,False)
    time.sleep(0.1)
    GPIO.output(TRIG,True)
    time.sleep (0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO_FC)==0:
        ps_FC=time.time()

    while GPIO.input(ECHO_FC)==1:
        pe_FC=time.time()

    #print "got start and end times, calculating distance now"
    pd_FC = pe_FC - ps_FC
    distance=pd_FC*17150/2
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
