########################################
#  Variables you might want to modify
########################################

HOSTNAME=learn.delaporte.us
# HOSTNAME=sydeswype
WWW_PASSWORD_FILE=/var/www/passwords

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

########################################
#  Database tasks
########################################

backup_database:
	ansible $(HOSTNAME) -m fetch -a "flat=yes dest=./db.sqlite3 src=/var/www/weekend-plans/db.sqlite3"

migrate: venv database
	$(VPYTHON) $(BASEDIR)/manage.py migrate

whut: venv 
	$(VPYTHON) $(BASEDIR)/manage.py schemamigration --auto weekend

init_south: venv 
	$(VPYTHON) $(BASEDIR)/manage.py schemamigration --initial weekend


########################################
#  Deployment Tasks
########################################


git_push:
	git push

deploy: git_push
	ansible-playbook playbook.yml --extra-vars="hosts=$(HOSTNAME)"

fix: git_push
	ansible-playbook playbook.yml --tags=fixed --extra-vars="hosts=$(HOSTNAME)"

restart_apache:
	ansible $(HOSTNAME) -m service -a "name=httpd state=restarted"

stop_apache:
	ansible $(HOSTNAME) -m service -a "name=httpd state=stopped"

set_password:
	ssh $(HOSTNAME) 'htpasswd -b -c $(WWW_PASSWORD_FILE) $(USERNAME) $(PASSWORD)'

# Call it like this:
#      make set_password USERNAME=leslie PASSWORD=12345
