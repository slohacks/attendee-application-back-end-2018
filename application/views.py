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