import time
import r3c
from r3s import get_dist


print "sensor readings start"
r3s.get_dist()
print "sensor readings end"

print "test start"
r = r3c.r3c() #initialize chassis
r.journey()

'''
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
'''

print "test over!"
