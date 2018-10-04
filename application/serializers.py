from rest_framework import serializers, permissions
from application.models import Application, Resume
from django.contrib.auth.models import User
from rest_framework import permissions



class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Application
       fields = ('id','first_name', 'last_name', 'email', 
       'phone_number','is_eighteen', 'school', 'graduation_date', 'major',
        'city', 'dietary_restrictions', 'allergies', 'github', 'linkedin',
        'personal_website', 'short_answer', 'gender', 'ethnicity',
        'anything_else', 'agreed')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password')
class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = ('resume',)
