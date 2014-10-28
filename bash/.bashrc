umask 022

export SERVICE=security-tools

export PATH=$PATH:/services/$SERVICE/sdg/share/python/django/bin:/home/settings

export PYTHONPATH=/services/$SERVICE/sdg/share/python/django:/services/$SERVICE/share/python:/usr/lib/python2.6/site-packages:/usr/lib64/python2.6/site-packages

export PYTHONSTARTUP=/home/ejtravis/settings/pytools.py
export PYLINTRC=/home/ejtravis/settings/pylint/.pylintrc
export LS_COLORS='di=36'
