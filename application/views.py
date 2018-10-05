from __future__ import unicode_literals
from application.models import Application
from application.serializers import ApplicationSerializer, UserSerializer
from rest_framework import generics, renderers, viewsets, permissions, status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, action, parser_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# Create your views here.
@api_view(['GET', 'POST'])
@parser_classes(( JSONParser, MultiPartParser, FormParser))
def application_list(request, format=None):
    if request.method == 'GET':
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        queryset = Application.objects.all()
        if serializer.is_valid():
            serializer.save(resume = request.data.get('resume'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes((JSONParser, MultiPartParser, FormParser))
def application_detail(request, pk, value=None, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if value:
            data = getattr(application, value)
            return Response(data)
        else:
            serializer = ApplicationSerializer(application)
            return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApplicationSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save(resume = request.data.get('resume'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class ApplicationViewSet(viewsets.ModelViewSet):
#     queryset = Application.objects.all()
#     serializer_class = ApplicationSerializer
#     parser_classes = (MultiPartParser, FormParser, JSONParser)
#     #permissions = (permissions.IsAuthenticatedOrReadOnly)
#     def perform_create(self, serializer):
#         serializer.save(resume = self.request.data.get('resume'))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    def perform_create(self, serializer):
        serializer.save()

@api_view(['GET'])
def questions(request):
    if request.method == 'GET':
        return Response({
            "body": 
                [
                    {
                    "id": 0,
                    "name": "Personal Info",
                    "questions":
                    [
                        {         
                        "id": "name",
                        "title": "What is your name?",
                        "inputType": 0
                        },
                        {          
                        "id": "email",
                        "title": "What is your email?",
                        "inputType": 1
                        },
                        {          
                        "id": "age",
                        "title": "Will you at least be 18 years old before February 1, 2019",
                        "inputType": 2,
                        "options": ["Yes", "No"]
                        },
                        {          
                        "id": "college",
                        "title": "What college do you attend?",
                        "inputType": 3
                        }
                    ]
                    },
                    {
                    "id": 1,
                    "name": "Basic Info",
                    "questions":
                    [
                        {         
                        "id": "resume",
                        "title": "Upload your resume.",
                        "inputType": 4
                        },
                        {          
                        "id": "github",
                        "title": "What is your Github?",
                        "inputType": 0
                        },
                        {          
                        "id": "project",
                        "title": "Tell us about one of the projects you're most proud of. Doesn't have to be CS-related",
                        "inputType": 0
                        }
                    ]
                    }
                ]
            })