import os
import time
from skeleton import *

os.system('/home/pi/PiBits/ServoBlaster/user/servod --p1pins=12 --pcm')
s = Skeleton() 
s.automode()

