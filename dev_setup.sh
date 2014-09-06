#!/bin/bash
virtualenv ENV
source activate.sh
pip install -r requirements.txt
# ./main/manage.py syncdb
