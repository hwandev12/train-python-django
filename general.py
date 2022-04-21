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
