from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Application(models.Model):
   XS = 0
   SMALL = 1
   MEDIUM = 2
   LARGE = 3
   XL = 4
   SIZES = (
       (XS, 'x-small'),
       (SMALL, 'small'),
       (MEDIUM, 'medium'),
       (LARGE, 'large'),
       (XL, 'x-large')
   )
   created = models.DateTimeField(auto_now_add = True)
   first_name = models.CharField(max_length = 30)
   last_name = models.CharField(max_length = 30)
   school = models.CharField(max_length = 250)
   t_shirt = models.IntegerField(default = XS, choices = SIZES)
   dob = models.DateField()
   resume = models.TextField()
   agreed = False
   owner = models.ForeignKey('auth.User', related_name = 'application', on_delete = models.CASCADE)
   objects = models.Manager()
   class Meta:
       ordering = ('created',)
       