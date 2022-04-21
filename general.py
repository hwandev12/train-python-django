# This is how to connect static files
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

# This is how to connect email send backend here
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
