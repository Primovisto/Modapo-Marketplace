from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_BXMhGZbzUnHrO4wR2QDrLSN1')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_L2u1PAnN0QLTVcbLRes1qB2W')


# PayPal Settings
SITE_URL = 'modapomarketplace.herokuapp.com'
PAYPAL_NOTIFY_URL = 'http://e1836b31.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'edward@primovisto.com'
