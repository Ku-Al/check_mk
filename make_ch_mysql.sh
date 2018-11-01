#!/bin/bash 

mysql --defaults-extra-file=/etc/check_mk/mysql.cfg -H -e 'SHOW ENGINE INNODB STATUS' > /var/tmp/innodb_status

