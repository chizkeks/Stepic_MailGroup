﻿﻿sudo pip install pymysql
sudo pip3 install django mysqlclient
sudo /etc/init.d/mysql start
mysql -uroot -e "create database if not exists ask_answer"
mysql -uroot -e "CREATE USER 'ipweb'@'localhost' IDENTIFIED BY 'qazmlp6';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'ipweb'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
python ~/web/ask/manage.py makemigrations qa
python ~/web/ask/manage.py migrate
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart