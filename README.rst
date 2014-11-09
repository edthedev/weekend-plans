
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
Edit your .ssh/config to add your host, port and user. This recipe expects that user to have some privileges, naturally.
Edit /etc/ansible/hosts to add your host (your can use the shortname from you .ssh/config)
Edit Makefile to update the hostname there, as well (you can also use the shortname here...)
Edit playbook.yml for either Debian or CentOS (uncomment the appropriate variables and apt or yum section)

Deploy the app::

    make deploy
    # (optional)
    # push local copy of database up...
    make set_password USERNAME=bob PASSWORD=12345

Manually copy the httpd.conf.example bit into the httpd.conf.::

    scp httpd.conf.example ansible-host:~
    ssh ansible-host
    # Debian
    cat ~/httpd.conf.example >> /etc/apache2/apache2.conf
    # CentOS
    cat ~/httpd.conf.example >> /etc/httpd/conf/httpd.conf
