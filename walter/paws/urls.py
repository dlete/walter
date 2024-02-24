# Core Django imports
from django.conf.urls import url

# This project apps imports
from . import views


urlpatterns = [

    # ex: /paws/clientdb_client_one/
    url(r'^clientdb_client_one/$', views.clientdb_client_one, name='clientdb_client_one'),

    # ex: /paws/csd_customer_one/
    url(r'^csd_customer_one/$', views.csd_customer_one, name='csd_customer_one'),

    # ex: /paws/csd_eline_all_fault/
    url(r'^csd_eline_all_fault/$', views.csd_eline_all_fault, name='csd_eline_all_fault'),

    # ex: /paws/csd_eline_one/
    url(r'^csd_eline_one/$', views.csd_eline_one, name='csd_eline_one'),

    # ex: /paws/mail_send/
    url(r'^mail_send/$', views.mail_send, name='mail_send'),



    # ex: /paws/saint2year/
    url(r'^saint2year/$', views.saint2year, name='saint2year'),

    # ex: /paws/year2city/
    url(r'^year2city/$', views.year2city, name='year2city'),

]

