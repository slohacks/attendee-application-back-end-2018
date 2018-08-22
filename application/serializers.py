from rest_framework import serializers, permissions
from application.models import Application
from django.contrib.auth.models import User
from rest_framework import permissions



class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    github = serializers.URLField(max_length = 250)
    linkedin = serializers.URLField(max_length = 250)
    def validate_github(self, value):
        print(type(value))
        print(value)
        if 'https://github.com/' not in value:
            raise serializers.ValidationError('Invalid Github link,' +
                ' please make sure that the link contains http://github.com/')
        return value
    def validate_linkedin(self, value):
        print(type(value))
        print(value)
        if 'https://www.linkedin.com/in/' not in value:
            raise serializers.ValidationError('Invalid LinkedIn link, ' +
                'please make sure that the link contains http://linkedin.com/in/')
        return value
    class Meta:
       model = Application
       fields = ('url', 'id','first_name', 'last_name', 'email', 
       'phone_number','is_eighteen', 'school', 'graduation_date', 'major',
        'city', 'dietary_restrictions', 'allergies', 'github', 'linkedin',
        'personal_website', 'resume', 'short_answer', 'gender', 'ethnicity',
        'anything_else', 'agreed')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password')
