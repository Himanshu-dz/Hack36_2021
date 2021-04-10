from django.db import models

# Create your models here.

class doctorsAccount(models.Model):
    name = models.CharField(max_length=100)
    profilePicture = models.ImageField(upload_to='profile_pic')
