import os

from django.core.wsgi import get_wsgi_application

# set dev environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings.dev")

application = get_wsgi_application()
