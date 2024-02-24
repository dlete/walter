These instructions assume Ubuntu 16.04

### Virtual environment
* Install Ubuntu package `python3-venv`
`sudo apt-get install python3-venv`

* Create the virtual environment
`python3 -m venv `</path/to/new/virtual/environment>`

* To operate in the virtual environment
`source </path/to/new/virtual/environment>/bin/activate`

* To, not use a virtualenv anymore
`deactivate <virtualenv>`


### Get the code
`git clone git@git.heanet.ie:heanet/walter.git`

### Install MySQL
* Install
`sudo apt-get install mysql-server libmysqlclient-dev`
Note: Unless libmysqlclient-dev is installed in the OS, the Python package 'mysqlclient' fill fail. The Python package 'mysqlclient' will be defined in the requirements.txt file. Do not worry about that Python package now.

* Create database, user and grant permissions:
`
CREATE DATABASE walter_prod CHARACTER SET UTF8;
CREATE USER 'walter'@'localhost' IDENTIFIED BY 'Friday13';
GRANT ALL PRIVILEGES ON walter_prod.* TO 'walter'@'localhost';
FLUSH PRIVILEGES;
`

* and then, for testing:
`
GRANT ALL PRIVILEGES ON test_walter_prod.* to 'walter'@'localhost';
`
Why? Because [The default test database names are created by prepending test_ to the value of each NAME in DATABASES](https://docs.djangoproject.com/en/1.11/topics/testing/overview/#the-test-database)

* and finally, verify:
`
    show grants for 'walter'@'localhost';
`

### Install required Python packages
* Within the virtuallenv. First of all
`pip install wheel`
* And now the Python packages 
`pip install -r requirements.txt`


### Initialize the Django project
Again, within the virtualenv. From now now, always operate within the
virtualenv.
`
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
`

### Install Apache2
* You will need these packages:
`
    sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
`

* copy the apache config file for the vhost to sites-available
* review apache config file for the vhost and ensure these parameters are correctly set for your environment:
`
WSGIDaemonProcess torque python-home=/workspace/virtualenvs/walter python-path=/workspace/pjt_walter/walter
WSGIProcessGroup walter
WSGIScriptAlias / /workspace/pjt_walter/walter/walter/wsgi.py
`
* soft link (ln -s) apache config file from sites-available to sites-enabled
* copy .htpasswd to /etc/apache2


## References
* http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-mysql-for-django
* https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04
* https://stackoverflow.com/questions/27274987/how-to-configure-and-use-mysql-with-django
* https://stackoverflow.com/questions/14186055/django-test-app-error-got-an-error-creating-the-test-database-permission-deni

* [How To Serve Django Applications with Apache and mod_wsgi on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04)
* [How To Set Up Password Authentication with Apache on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-password-authentication-with-apache-on-ubuntu-16-04)


### Favicon
* Create picture with Gimp and save as *.xcf
* In Gimp, go to File -> Export or Export as...
* Export as *.png
* Put in the static folder
* Link to it from base.html
