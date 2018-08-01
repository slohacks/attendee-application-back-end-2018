from rest_framework import serializers, permissions
from application.models import Application
from django.contrib.auth.models import User
from rest_framework import permissions



class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Application
       fields = ('url', 'id','first_name', 'last_name', 'school', 't_shirt',
                 'dob', 'resume')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('url', 'id','username')
