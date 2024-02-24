# Core Django imports
from django.conf.urls import url

# This project apps imports
from . import views


urlpatterns = [

    # This is the landing page
    # /core/
    url(r'^$', views.about, name='landing'),

    # ex: /core/about/
    url(r'^about/$', views.about, name='about'),

]

