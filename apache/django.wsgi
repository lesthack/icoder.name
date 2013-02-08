import os
import sys

sys.path.append('/home/lesthack/public_html/')
sys.path.append('/home/lesthack/public_html/icoder_name/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'icoder_name.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
