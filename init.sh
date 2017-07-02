sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
sudo apt-get install python3-dev
﻿﻿sudo pip install pymysql
sudo pip3 install django mysqlclient

sudo /etc/init.d/mysql start
mysql -uroot -e "create database myproject;"
mysql -uroot -e "CREATE USER 'enth'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'enth'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
sudo gunicorn --bind=0.0.0.0:8000 ask.wsgi:application &