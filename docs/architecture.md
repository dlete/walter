## Django REST Framemwork (DRF)
* Install the DRF package. 
`pip install djangorestframework`

* To customize navigation bar: edit rest_framework/base.html
* To customize login page: edit rest_framework/login_base.html

* Create dedicated app
`python manage.py startapp apiv1`

* Url in project points to app

#### Authentication
You can't really leave an API exposed without authentication. Best thing to do is to:
* Require DRF for the user to authenticate
* Make Apache WSGI to proxy, to pass the authentication that is required to access the site (API or not) anyway to DRF. You do this with the setting `WSGIPassAuthorization On` in the Apache config file.

### To authentication
* add `url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))` to walter/urls.py
* add, in walter/settings.py
`
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
}
`


### Django REST Swagger
* Python package
`$ pip install django-rest-swagger`

* Add 'rest_framework_swagger' to INSTALLED_APPS in Django settings.
`
INSTALLED_APPS = [
    ...
    'rest_framework_swagger',
    ...
]
`

* Update urls.py of Django project, `walter/urls.py` in this case
`

* Update statics of DRF and Swagger
`python manage.py collectstatic`


# Core Django imports
from django.conf.urls import url

# Third-party app imports
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Walter API')

urlpatterns = [

    # Django REST Swagger
    url(r'^api-doc/', schema_view),

]
`
