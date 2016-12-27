import time
import r3c
from r3s import get_dist, get_sensorpin


print "test start, initializing chasis and sensors"
r = r3c.r3c() #initialize chassis

print "@@@@@@@@@@ sensor readings start"
for x in range(0, 90):
    print "Reading #: ",x
'''    get_dist('fl')
    time.sleep(1)
    get_dist('fc')
    time.sleep(1)
    get_dist('fr')
    time.sleep(1)'''
    get_dist('fc')    
    print "\n\n"

print "@@@@@@@@@@ sensor readings end"
