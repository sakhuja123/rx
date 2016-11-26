import time
import r3c
from r3s import get_dist

print "test start"
r = r3c.r3c() #initialize chassis

r.nav(65,65,10)
r.nav(-65,-65,10)
r.pivot('left')
r.pivot('right')

print "test over!"
