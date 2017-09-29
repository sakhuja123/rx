import time
import r3c
from r3s import get_dist, get_sensorpin


print "test start, initializing chasis and sensors"
r = r3c.r3c() #initialize chassis

print "@@@@@@@@@@ START WHEEL TEST"
r.wheel_test()
print "@@@@@@@@@@ STOP WHEEL TEST"

print "@@@@@@@@@@ test random journey start"
print "@@@@@@@@@@ test random journey start"
print "@@@@@@@@@@ test random journey start"
print "@@@@@@@@@@ test random journey start"
print "@@@@@@@@@@ test random journey start"
print "@@@@@@@@@@ test random journey start"
#r.move(50,50)
#r.journey('random',90)
print "@@@@@@@@@@ test random journey end"
print "@@@@@@@@@@ test random journey end"
print "@@@@@@@@@@ test random journey end"
print "@@@@@@@@@@ test random journey end"
print "@@@@@@@@@@ test random journey end"


print "nav front 3secs back 3secs"
r.nav(-100,-100,-3)
r.nav(100,100,3)
r.stop()
print "STOPPING nav front 3secs back 3secs"


print "pivot left"
r.pivot('left')
time.sleep(2)
print "pivot right"
r.pivot('right')

print "fwd"
r.nav(65,65,5)
print "backup"
r.nav(-65,-65,5)

print "test over!"
