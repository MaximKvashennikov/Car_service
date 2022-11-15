SECRET_KEY = "django-insecure-d!-j-a)ttcp*itk(10y@7%ieeua17uei(_6ye!1n$o4mqg3@v%"

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'car_service_db',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
