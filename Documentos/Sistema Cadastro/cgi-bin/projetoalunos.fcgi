#!/usr/bin/python2.6 

import sys, os

sys.path.insert(0, "/afs/cern.ch/user/t/tilecom/www/django/flup-1.0.2-py2.6.egg")
sys.path.insert(0, "/afs/cern.ch/user/t/tilecom/www/test-lps/projetoalunossite") 
sys.path.insert(0, "/afs/cern.ch/user/t/tilecom/www/django")

os.environ['DJANGO_SETTINGS_MODULE'] = "mysite.settings" 

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
