
Setting up
-----------
To setup from source the first time, remember these steps::

    git clone https://github.com/edthedev/weekend-plans.git
    cd weekend-plans
    make venv
    make database

To run the local server::
    
   make runserver 

Deploying
----------
Edit playbook.yml for either Debian or CentOS.

    make deploy
    # (optional)
    # push local copy of database up...
    make set_password USERNAME=bob PASSWORD=12345

