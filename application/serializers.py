from rest_framework import serializers, permissions
from application.models import Application
from django.contrib.auth.models import User
from rest_framework import permissions



class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    # Fields that need validation
    github = serializers.URLField(max_length = 250)
    linkedin = serializers.URLField(max_length = 250)
    graduation_date = serializers.DateField()
    is_eighteen = serializers.BooleanField(default = False)
    agreed = serializers.BooleanField(default = False)
    # Validators for fields
    def validate_github(self, value):
        if 'https://github.com/' not in value:
            raise serializers.ValidationError('Invalid Github link,' +
                ' please make sure that the link contains http://github.com/')
        return value
    def validate_linkedin(self, value):
        if 'https://www.linkedin.com/in/' not in value:
            raise serializers.ValidationError('Invalid LinkedIn link, ' +
                'please make sure that the link contains http://linkedin.com/in/')
        return value
    def validate_graduation_date(self, value):
        year = 2019
        month = 2
        day = 3
        if value.year < year:
            raise serializers.ValidationError(
                'Invalid Date: Applicant graduated before the event')
        elif value.year == year:
            if value.month < month:
                raise serializers.ValidationError(
                    'Invalid Date: Applicant graduated before the event')
            if value.month == month:
                if value.day <= day:
                    raise serializers.ValidationError(
                        'Invalid Date: Applicant graduated before the event')
        return value
    def validate_is_eighteen(self, value):
        if not value:
            raise serializers.ValidationError('Invalid Age: Applicant must be 18')
        return value
    def validate_agreed(self, value):
        if not value:
            raise serializers.ValidationError('Invalid: Applicant must agree' + 
            ' to the code of conduct')

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
