import os, sys
import os.path

root_path = os.path.abspath(os.path.split(__file__)[0])

sys.path.insert(0, os.path.join(root_path, 'www_tatoeba'))
sys.path.insert(0, root_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'www_tatoeba.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

