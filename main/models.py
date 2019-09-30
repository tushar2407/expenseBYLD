from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
'''class Profile(User):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.user.first_name
'''
class File(models.Model):
    name=models.CharField(max_length=256)
    path=models.FileField()
    #user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
'''
class User(models.Model):
    name=User.first_name
    username=User.username
    def __str__(self):
        return self.name '''
