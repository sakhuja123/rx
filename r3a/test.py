import time
import r3c
from r3s import get_dist

print "test start"
r = r3c.r3c() #initialize chassis

print "nav test 30 secs"
r.nav(65,65,30)

'''
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
