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
#  Deployment Tasks
########################################

backup_database:
	ansible $(HOSTNAME) -m fetch -a "dest=. src=/var/www/weekend-plans/db.sqlite3"

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
