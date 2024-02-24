# Core Django imports
from django.conf.urls import url
from django.conf.urls import include

# Third-party app imports
from rest_framework import routers

# This project apps imports
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Client DB
    # ex: /clientdb/clientdb_client_one/
    url(r'^clientdb/clientdb_client_one/(?P<client_id>[0-9]+)/$',
        views.clientdb_client_one.as_view()
    ),

    #""" CSD """
    # ex: /csd/csd_customer_one/
    url(r'^csd/csd_customer_one/(?P<customer_identity>[0-9]+)/$',
        views.csd_customer_one.as_view()
    ),

    # ex: /csd/csd_eline_all_fault/
    url(r'^csd/csd_eline_all_fault/(?P<fault_status>[\w\-]+)/$',
        views.csd_eline_all_fault.as_view()
    ),

    # ex: /csd/csd_eline_one/
    url(r'^csd/csd_eline_one/(?P<eline_identity>[0-9]+)/$',
        views.csd_eline_one.as_view()
    ),


    # Mail
    # ex: /mail/mail_send/
    url(r'^mail/mail_send/(?P<mail_to>[\w\-]+)/(?P<mail_subject>[\w\-]+)/(?P<mail_body>[\w\-]+)/$',
        views.mail_send.as_view()
    ),

    #""" Labs """
    # ex: /labs/saint2year/
    url(r'^labs/saint2year/(?P<saint_name>[\w\-]+)/$',
        views.saint2year.as_view()
    ),

    # ex: /labs/year2city/
    url(r'^labs/year2city/(?P<games_year>[0-9]+)/$',
        views.year2city.as_view()
    ),

]
