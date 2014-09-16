# When you are playing around with the app and you expect that an email should
# have been sent, just run `./manage.py send_mail` and you will get the mail
# to the ADMINS account, no matter who the real recipient was.
#MAILER_EMAIL_BACKEND = 'django_libs.test_email_backend.EmailBackend'
#TEST_EMAIL_BACKEND_RECIPIENTS = ADMINS
#FROM_EMAIL = ADMINS[0][1]
#EMAIL_SUBJECT_PREFIX = '[dev yourprojectname] '
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'zss.appdragon@gmail.com'
# Enter your gmail PW from the ADMINS email entered above.
EMAIL_HOST_PASSWORD = 'simon1234'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'zss.appdragon@gmail.com '

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

HELPDESK_EMAIL = 'zss.appdragon@gmail.com'


#ACCOUNT_EMAIL_VERIFICATION = "none"

