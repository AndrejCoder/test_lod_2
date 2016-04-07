"""
WSGI config for test_lod_2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys, site

root = os.path.dirname(os.path.abspath(__file__))
extra_path = os.path.join(root, '../../ve/lib/python2.7/site-packages')
sys.path = [extra_path, os.path.dirname(root), root] + sys.path

site.addsitedir(extra_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_lod_2.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()