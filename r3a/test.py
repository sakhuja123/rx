import time
import r3c
from r3s import get_dist

r3 = r3c.r3c() #initialize chassis

r3.nav(50,50,30)
time.sleep(3)
r3.nav2(50,50,30)
