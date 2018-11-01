#!/usr/bin/env python3

import re

file = '/var/tmp/innodb_status'
WAR = 20
CRIT = 10
STATUS = 0
STATUSTXT = 'OK'

pat2 = re.compile('Buffer pool size\s+(\d+)')
pat3 = re.compile('Free buffers\s+(\d+)')

f = open(file, "r")
strf = f.read()

buf = re.search(pat2, strf)
fbuf = re.search(pat3, strf)

if buf!=None and fbuf!=None:
    bufsize = buf.group(1)
    freebufsz = fbuf.group(1)
    
    bufsizepr = int(freebufsz)*100/int(bufsize)
    if bufsizepr < WAR: 
        STATUS = 1
        STATUSTXT = 'WARNING'
    if bufsizepr < CRIT: 
        STATUS = 2
        STATUSTXT = 'CRITICAL'
else:
    bufsize = -1
    freebufsz = -1
    bufsizepr = -1
    STATUS = 3
    STATUSTXT = 'UNKNOWN'
    
print("{0} Buffer_innodb_size currfreeBufFree={1:0.2f}%;{2};{3} {4} - {1:0.2f}% current values {5}".format(STATUS, bufsizepr,WAR,CRIT,STATUSTXT,freebufsz))
