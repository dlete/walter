# Core Django imports
from django.shortcuts import render
from django.contrib.auth.models import User, Group

# Third-party app imports
from rest_framework import viewsets

# This project apps imports
#from walter.apiv1.serializers import UserSerializer, GroupSerializer
from .serializers import UserSerializer
from .serializers import GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = User.objects.all().order_by('-date_joined')
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Core Django imports
#from django.db import models

# Third-party app imports
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

class saint2year(APIView):
    def get(self, request, saint_name, format=None):
        from paws.libs.labs import one2one
        saint_year = one2one.saint2year(saint_name)
        int_saint_year = int(saint_year)
        return Response(int_saint_year)

class year2city(APIView):
    def get(self, request, games_year, format=None):
        from paws.libs.labs import one2one
        games_city = one2one.year2city(games_year)
        str_games_city = str(games_city)
        return Response(str_games_city)


class clientdb_client_one(APIView):
    def get(self, request, client_id, format=None):
        from paws.libs.clientdb import clientdb_get_client_one
        client = clientdb_get_client_one.clientdb_client_one_tech(client_id)
        return Response(client)

class csd_customer_one(APIView):
    def get(self, request, customer_identity, format=None):
        from paws.libs.csd import csd_get_customer_one_detail
        customer = csd_get_customer_one_detail.csd_customer_detail(customer_identity)
        return Response(customer)

class csd_eline_all_fault(APIView):
    def get(self, request, fault_status, format=None):
        from paws.libs.csd import csd_get_eline_all_by_fault_status
        elines = csd_get_eline_all_by_fault_status.csd_elines_by_fault_status(fault_status)
        return Response(elines)

class csd_eline_one(APIView):
    def get(self, request, eline_identity, format=None):
        from paws.libs.csd import csd_get_eline_one_detail
        eline = csd_get_eline_one_detail.csd_eline_detail(eline_identity)
        return Response(eline)

class mail_send(APIView):
    def post(self, request, mail_to, mail_subject, mail_body, format=None):
        message = "Hola"
        return Response(eline)
