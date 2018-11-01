#!/bin/bash

DIR=/home/anton/www/
status=0
statustxt=OK

count=$(find $DIR -type f -mmin -10 |  wc -l)

if [ $count -gt 40 ] 
then
     status=2
     statustxt=CRITICAL
     find $DIR -type f -mmin -10 | xargs ls -l > /var/tmp/new_files
elif [ $count -gt 10 ] 
then
     status=1
     statustxt=WARNING
     find $DIR -type f -mmin -10 | xargs ls -l > /var/tmp/new_files
fi

echo "$status new_file count=$count;10;40 $statustxt - $count new file in $DIR"
 
