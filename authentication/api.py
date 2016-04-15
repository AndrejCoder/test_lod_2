# coding: utf-8
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.permissions import IsAuthenticatedOrCreate
from authentication.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrCreate, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
