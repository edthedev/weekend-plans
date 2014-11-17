########################################
#  Variables you might want to modify
########################################

# HOSTNAME=learn.delaporte.us
HOSTNAME=ansible-ratchet
WWW_PASSWORD_FILE=/var/www/passwords

# Debian
APACHE_SVC=apache2
# Centos
# APACHE_SVC=httpd

########################################
#  Computed variables
########################################

BASEDIR=$(PWD)
VPYTHON=$(BASEDIR)/ENV/bin/python

########################################
#  Development Tasks
########################################

venv: requirements.txt
	test -d $(BASEDIR)/ENV || virtualenv $(BASEDIR)/ENV 
	$(BASEDIR)/ENV/bin/pip install -r requirements.txt

database: venv 
	$(VPYTHON) $(BASEDIR)/manage.py syncdb

runserver: venv database
	$(VPYTHON) $(BASEDIR)/manage.py runserver

open:
	open http://127.0.0.1:8000/

########################################
#  Database tasks
########################################

backup_database:
	ansible $(HOSTNAME) -m fetch -a "flat=yes dest=./db.sqlite3 src=/var/www/weekend-plans/db.sqlite3"

upload_database:
	ansible $(HOSTNAME) -m copy -a "src=./db.sqlite3 dest=/var/www/weekend-plans/db.sqlite3"

# Django 1.7 migrate: venv database
#$(VPYTHON) $(BASEDIR)/manage.py migrate

migrate: venv 
	$(VPYTHON) $(BASEDIR)/manage.py migrate

init_south_shopping: venv 
	$(VPYTHON) $(BASEDIR)/manage.py schemamigration --initial shopping


########################################
#  Deployment Tasks
########################################

git_push:
	git push

deploy: git_push
	ansible-playbook -vv playbook.yml --extra-vars="hosts=$(HOSTNAME)"

fix: git_push
	ansible-playbook playbook.yml --tags=fixed --extra-vars="hosts=$(HOSTNAME)"

restart_apache:
	ansible $(HOSTNAME) -m service -a "name=$(APACHE_SVC) state=restarted"

stop_apache:
	ansible $(HOSTNAME) -m service -a "name=$(APACHE_SVC) state=stopped"

set_password:
	ssh $(HOSTNAME) 'htpasswd -b -c $(WWW_PASSWORD_FILE) $(USERNAME) $(PASSWORD)'

# Call it like this:
#      make set_password USERNAME=leslie PASSWORD=12345
#

