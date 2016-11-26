import time
import r3c
from r3s import get_dist

print "test start"
r = r3c.r3c() #initialize chassis

print "fwd"
r.nav(65,65,5)
print "backup"
r.nav(-65,-65,5)
print "pivot left"
r.pivot('left')
print "pivot right"
r.pivot('right')

print "test over!"
