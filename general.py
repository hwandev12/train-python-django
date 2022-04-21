# This is how to connect static files
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

# This is how to connect email send backend here
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# This is how login, logout work with urls here
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

# This is how to connect the outside of the frontend folder
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Here we can see
        'DIRS': [ BASE_DIR / 'frontend' ],
        # Here we can see
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
