"""
Django settings for yata project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from decouple import config
from yata.handy import datestr

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
print(f"[YATA {datestr()}] settings DEBUG={DEBUG}")

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY set in config variables
SECRET_KEY = config('SECRET_KEY')
print(f"[YATA {datestr()}] settings SECRET_KEY={SECRET_KEY}")

ALLOWED_HOSTS = [config('ALLOWED_HOSTS', default="*")]
print(f"[YATA {datestr()}] settings ALLOWED_HOSTS={ALLOWED_HOSTS}")

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'player.apps.PlayerConfig',
    'awards.apps.AwardsConfig',
    'target.apps.TargetConfig',
    'chain.apps.ChainConfig',
    'faction.apps.FactionConfig',
    'bazaar.apps.BazaarConfig',
    'stocks.apps.StocksConfig',
    'company.apps.CompanyConfig',
    'loot.apps.LootConfig',
    'setup.apps.SetupConfig',
    'bot.apps.BotConfig',
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django_extensions',
    'mathfilters',
    'django_json_widget',
    'redisboard',
    'rest_framework'
]

MIDDLEWARE = [
    'player.middleware.ip_middleware.XForwardedForMiddleware',
    'django_brotli.middleware.BrotliMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

ROOT_URLCONF = 'yata.urls'

if DEBUG:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'yata.context_processors.sectionMessage',
                    'yata.context_processors.nextLoot',
                ],
            },
        },
    ]
else:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'yata.context_processors.sectionMessage',
                    'yata.context_processors.nextLoot',
                ],
                'loaders': [(
                    'django.template.loaders.cached.Loader', [
                        'django.template.loaders.app_directories.Loader',
                        'django.template.loaders.filesystem.Loader',
                    ]
                )]
            },
        },
    ]


WSGI_APPLICATION = 'yata.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if config("DATABASE", default="sqlite", cast=str) == "postgresql":
    print(f"[YATA {datestr()}] settings DATABASE=postgresql")
    conn_max = config("PG_CONN_MAX_AGE", cast=int, default=600)
    print(f"[YATA {datestr()}] settings CONN_MAX_AGE={conn_max}")

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config("PG_NAME"),
            'USER': config("PG_USER"),
            'PASSWORD': config("PG_PASSWORD"),
            'HOST': config("PG_HOST"),
            'PORT': config("PG_PORT"),
            'CONN_MAX_AGE': conn_max,
        }
    }

else:
    print(f"[YATA {datestr()}] settings DATABASE=sqlite3")

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Cache
# https://docs.djangoproject.com/en/3.1/topics/cache/


def get_cache():
    import os
    if (config('USE_REDIS', default=False, cast=bool)):
        print(f"[YATA {datestr()}] settings CACHE=redis")

        return {
            'default': {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": config('REDIS_HOST'),
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                    "PASSWORD": config('REDIS_PASSWORD'),
                }
            }
        }

    else:
        print(f"[YATA {datestr()}] settings CACHE=DB")

        return {
            'default': {
                'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
                'LOCATION': 'cache',
            }
        }


CACHES = get_cache()


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },


]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# where to collect
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'), )

# where to look for
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# sentry
if config("ENABLE_SENTRY", default=False, cast=bool):
    SENTRY = True
    print(f"[YATA {datestr()}] settings SENTRY=ENABLED")

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=config("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        send_default_pii=True,
        traces_sample_rate=config("SENTRY_SAMPLE_RATE", default=0.0, cast=float),
        environment=config("SENTRY_ENVIRONMENT"),
    )
else:
    SENTRY = False


#  src directory
SRC_ROOT = os.path.join(PROJECT_ROOT, 'src')
