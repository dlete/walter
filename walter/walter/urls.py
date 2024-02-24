"""walter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# Core Django imports
from django.conf.urls import  include
from django.conf.urls import url
from django.contrib import admin

# Third-party app imports
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Walter API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^core/', include('core.urls', namespace="core")),

    # pointer to app paws
    url(r'^paws/', include('paws.urls', namespace="paws")),

    # For landing page
    # https://tutorial.djangogirls.org/en/django_urls/
    url(r'', include('core.urls')),

    # Django REST Framework
    # e.g. /api/v1/
    url(r'^api/v1/', include('apiv1.urls', namespace="apiv1")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    # Django REST Swagger
    url(r'^api-doc/', schema_view),

]
