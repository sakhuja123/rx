import time
import r3c
from r3s import get_dist, get_sensorpin


print "test start, initializing chasis and sensors"
r = r3c.r3c() #initialize chassis


print "@@@@@@@@@@ test journey start"
r.move(50,50)
r.journey('random',90)
print "@@@@@@@@@@ test journey end"


print "nav test 60 secs"
r.nav(-100,-100,-1)
r.nav(100,100,60)
r.stop()

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
