#!/usr/bin/env python
# By Mahmoud Ashraf Abdelkader
# Linkedin: https://linkedin.com/in/mahmoud-abdelkader-417361204/
import os 
import time
import sys
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

for i in progressbar(range(15), "Loading: ", 40):
    time.sleep(0.7) # any calculation you need
          
cmd = 'cp /etc/passwd /root/LinuxPass/users.txt && cp /etc/shadow /root/LinuxPass/pass.txt && unshadow users.txt pass.txt > hash.txt && rm -rf users.txt pass.txt && john -w=/usr/share/wordlists/rockyou.txt hash.txt'

os.system(cmd)
