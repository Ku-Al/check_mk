## Скрипты для локальной обработки в chechk_mk

## Подсчет свободных буферов InnoDB
В кроне запускаем каждую минуту скрипт make_ch_mysql.sh 
Он формирует файл /var/tmp/innodb_status
Его уже обрабатывает локальный агент check_mk_innodb.py 

## Подсчет кол-ва экземпляров php-fpm
Стандартный плачин check_mk формирует файл /var/tmp/nginx_status
Его уже парсит check_mk_php.py 

## Проверка на новые файлы в директории
Локальный чекер check_mk_new_file.sh проверяет на появление новых файлов необходимые директории


