#!/bin/bash
pip install -r requirements.txt
./main/manage.py syncdb
