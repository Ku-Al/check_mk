#!/usr/bin/env python3

import re
file = '/var/tmp/nginx_status'
WAR = 80
CRIT = 90
STATUS = 0
STATUSTXT = 'OK'

f = open(file, "r")
pat1 = re.compile('listen queue:\s+(\d+)')
pat2 = re.compile('listen queue len:\s+(\d+)')
strf = f.read()
lq = re.search(pat1, strf)
lql = re.search(pat2, strf)

if lq!=None and lql!=None:
    listque = lq.group(1)
    listquelen = lql.group(1)
else:
    STATUS = 3
    STATUSTXT = 'UNKNOWN'
    listque = -1
    curpr = -1

if int(listque) == 0:
    STATUS = 0
    STATUSTXT = 'OK'
    curpr = 0
else:
    curpr = int(listque)*100/int(listquelen)
    if curpr > WAR: 
        STATUS = 1
        STATUSTXT = 'WARNING'
    if curpr > CRIT: 
        STATUS = 2
        STATUSTXT = 'CRITICAL'
print("{0} php_fpm_queue_len curpr={1:0.2f}%;{2}%;{3}% {4} - {1:0.2f} values {5}".format(STATUS, curpr,WAR,CRIT,STATUSTXT,listque))    
        
