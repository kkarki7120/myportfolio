from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.MOdel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    

