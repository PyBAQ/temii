from base import *
import dj_database_url

DEBUG = False
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'votos.wsgi_production.application'

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_KEY'),
    'release': raven.fetch_git_sha(os.path.abspath(os.pardir)),
}
