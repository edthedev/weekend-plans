BASEDIR=$(PWD)
VPYTHON=$(BASEDIR)/ENV/bin/python
HOSTNAME=learn.delaporte.us

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

deploy:
	ansible-playbook playbook.yml

fix:
	ansible-playbook playbook.yml --tags=fixed

restart_apache:
	ansible $(HOSTNAME) -m service -a "name=httpd state=restarted"

stop_apache:
	ansible $(HOSTNAME) -m service -a "name=httpd state=stopped"
