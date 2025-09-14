# ... usual Django settings

INSTALLED_APPS = [
    'accounts',  # Add the accounts app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ... rest of settings like MIDDLEWARE, TEMPLATES, DATABASES

AUTH_USER_MODEL = 'accounts.CustomUser'

# Static and media settings for profile_photo
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ... rest of your settings
