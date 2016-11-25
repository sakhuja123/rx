import time
import r3c

r3 = r3c.r3c()
print "moving"

r3.move(50,50,3)
print "navigating"

r3.nav(50,50,3)
time.sleep(1)
