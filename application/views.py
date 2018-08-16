from __future__ import unicode_literals
from application.models import Application
from application.serializers import ApplicationSerializer, UserSerializer
from rest_framework import generics, renderers, viewsets, permissions, status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    #permissions = (permissions.IsAuthenticatedOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(resume = self.request.data.get('resume'))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    def perform_create(self, serializer):
        serializer.save()