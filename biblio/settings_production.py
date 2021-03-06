# Django settings for biblio project.
from settings_default import *
UNIQUE_PREFIX = 'biblio_production'

DEPLOYMENT = {
    'git_repository': 'git@github.com:sspross/biblio.git',
    'git_branch': 'master',
    'git_remote': 'origin',
    'hosts': ['nexa.nine.ch'],
    'user': 'www-data',
    'project': 'biblio',
    'root': '/home/www-data/projects',
    'celery_worker': '%s_celery' % UNIQUE_PREFIX,
    'rabbitmq_vhost': UNIQUE_PREFIX,
    'rabbitmq_username': UNIQUE_PREFIX,
    'rabbitmq_password': '52d098vfn13',
    'is_stage': False,
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_%s' % UNIQUE_PREFIX,
        'USER': 'db',
        'PASSWORD': 'gevvemav',
        'HOST': '',
        'PORT': '',
    }
}

MIDDLEWARE_CLASSES += ('allink_essentials.middleware.validate_host_middleware.ValidateHostMiddleware',)

ADMINS = (
    ('itcrowd', 'itcrowd@allink.ch'),
)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': UNIQUE_PREFIX,
        'VERSION': 1,
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

# broker and celery
BROKER_URL = 'amqp://%(rabbitmq_username)s:%(rabbitmq_password)s@localhost:5672/%(rabbitmq_vhost)s' % DEPLOYMENT
CELERY_RESULT_BACKEND = "redis://localhost/0"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERYD_CONCURRENCY = 1
CELERY_SEND_EVENTS = False
CELERY_ENABLE_UTC = True

# sentry
RAVEN_CONFIG = {
    'dsn': 'https://508d92f5d1e242b39e8c04b9f80425e2:00508fa123d64e46b23adccc0a6dc190@sentry.allink.ch/29',
}
