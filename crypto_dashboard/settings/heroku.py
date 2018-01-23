DEBUG = False
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'cryptodashboard',
        'USER':'',
        'PASSWORD':'',
        'HOST':'localhost',

    }
}

import dj_database_url

DATABASES['default'] = dj_database_url.config()
