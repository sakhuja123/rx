≈Import RPi.GPIO
Import time
GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=24


Print “distance measurement in progress”


GPIO.setup(TRIG,GPIO.out)
GPIO.setup (ECHO,GPIO.in)
GPIO.output(TRIG,false)
Print "waiting for sensors”
time.sleep(2)


GPIO.output(TRIG,2)
time.sleep (0.00001)
GPIO.output(TRIG,false)


while GPIO.input(echo)==0;
    pulse_start=(time.time)


while GPIO.input(echo)==1;
    pulse_end=(time.time)


pulse_duration=pulse_end-pulse_start
distance=pulse_duration*17150
distance=round(distance,2)
print “distance”,distance,”cm"


GPIO.cleanup()

