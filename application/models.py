from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator

class Application(models.Model):
    #Dietary Restrictions
    none = 0
    kosher = 1 
    gluten_free = 2
    vegan = 3
    vegetarian = 4
    other_diet = 5
    DIET = (
        (none, 'None'),
        (kosher, 'Kosher'),
        (gluten_free, 'Gluten-Free'),
        (vegan, 'Vegan'),
        (vegetarian, 'Vegetarian'),
        (other_diet, 'Other')
    )
    #Genders
    female = 0 
    male = 1
    other_gender = 2
    GENDERS = (
        (female, 'Female'),
        (male, 'Male'),
        (other_gender, 'Other'),
    )
    #Ethnicites
    aian = 0
    asian = 1
    black = 2
    latino = 3
    nhopi = 4
    white = 5
    other_ethnicities = 6
    ETHNICITIES = (
        (aian, 'American Indian or Alaska Native'),
        (asian, 'Asian'),
        (black, 'Black or African American'),
        (latino, 'Hispanic or Latino'),
        (nhopi, 'Native Hawaiian or Other Pacific Islander'),
        (white, 'White'),
        (other_ethnicities, 'Other')
    )

    created = models.DateTimeField(auto_now_add = True)
    #Personal Information
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 250)
    phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$', 
     message = "Phone number must be entered" + 
     "in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators = [phone_regex], 
       max_length = 17, blank =True )
    is_eighteen = models.BooleanField(default = False)
    school = models.CharField(max_length = 250) 
    graduation_date = models.DateField()
    major = models.CharField(max_length = 250)
    city = models.CharField(max_length = 250)
    dietary_restrictions = models.IntegerField(default = none, choices = DIET)
    other_dietary_restrictions = models.TextField()
    allergies = models.TextField()
    #Basic Info
    github = models.URLField(max_length = 250)
    linkedin = models.URLField(max_length = 250)
    personal_website = models.URLField(max_length = 250)
    resume = models.FileField(upload_to='resume/',blank = False, null = False)
    #Short Answer
    short_answer = models.TextField()
    #Statistical Qustions
    gender = models.IntegerField(default = none, choices = GENDERS)
    other_gender_field = models.TextField()
    ethnicity = models.IntegerField(default = none, choices = ETHNICITIES)
    other_ethnicity = models.TextField()
    anything_else = models.TextField()
    agreed = models.BooleanField(default = False)
    #owner = models.ForeignKey('auth.User', related_name = 'application', on_delete = models.CASCADE)
    objects = models.Manager()
    class Meta:
        ordering = ('created',)
class User(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    username = models.CharField(max_length = 250)
    password = models.CharField(max_length = 250)
       