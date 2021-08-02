

import schedule
import time
import os
def ds():
    meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
    mem_kib = (meminfo['MemFree']/1024) 
    print("{}MB Free".format(mem_kib))

schedule.every(5).seconds.do(ds)   
while 1:
    schedule.run_pending()
    time.sleep(1)
