BASEDIR=$(PWD)
VPYTHON=$(BASEDIR)/ENV/bin/python

venv: requirements.txt
	test -d $(BASEDIR)/ENV || virtualenv $(BASEDIR)/ENV 
	$(BASEDIR)/ENV/bin/pip install -r requirements.txt

database: venv 
	$(VPYTHON) $(BASEDIR)/manage.py syncdb

runserver: venv database
	$(VPYTHON) $(BASEDIR)/manage.py runserver
