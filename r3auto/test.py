import time
import r3c

r3 = r3c.r3c()
print "moving"

r3.move(100,100,1)
print "navigating"

r3.nav(100,100,1)
time.sleep(1)
