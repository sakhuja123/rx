import time
import r3c
from r3s import get_dist

print "test start"
r3 = r3c.r3c() #initialize chassis

r3.nav(50,50,30) #autonmous navigation

print "test over!"
