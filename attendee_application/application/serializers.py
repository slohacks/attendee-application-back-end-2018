from rest_framework import serializers, permissions
from application.models import Application
from django.contrib.auth.models import User
from rest_framework import permissions



class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
   owner = serializers.ReadOnlyField(source = 'owner.username')
   class Meta:
       model = Application
       fields = ('url', 'id', 'first_name', 'last_name', 'school', 't_shirt',
                 'dob', 'resume', 'agreed', 'owner')
class UserSerializer(serializers.ModelSerializer):
    application = serializers.HyperlinkedRelatedField(many = True, view_name = 'application-detail', read_only = True)
    class Meta:
        model = User
        fields= ('url', 'id', 'username', 'application')
