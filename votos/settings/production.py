from .base import *
import dj_database_url

DEBUG = False
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers
ALLOWED_HOSTS = ['*']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# STATICFILES_DIRS = ( os.path.join(PROJECT_ROOT, 'static'),)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
