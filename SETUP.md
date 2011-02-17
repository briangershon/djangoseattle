GETTING STARTED
===============
1. Setup a virtual environment with Python 2.x (tested on Python 2.5)

        export PIP_REQUIRE_VIRTUALENV=true
        export PIP_RESPECT_VIRTUALENV=true
        
        cd /your-desired-virtualenv-folder
        virtualenv --no-site-packages djangoseattle_env
        
        cd djangoseattle_env
        source bin/activate
        ./bin/easy_install pip

2. Create a site

        [you should currently be in your /your-desired-virtualenv-folder]
        git clone git://github.com/briangershon/djangoseattle.git
        ./bin/pip install -r djangoseattle/requirements.txt
        
        ./bin/django-admin.py createproject site
        cd site
        chmod u+x manage.py

3. Setup a settings_local.py file by copying one of the samples.

4. Run `./manage.py syncdb` to create models

5. Run `./manage.py runserver` to see a working site on port 8080

