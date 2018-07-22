from __future__ import unicode_literals
from application.models import Application
from application.serializers import ApplicationSerializer
from rest_framework import generics, renderers, viewsets, permissions
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)