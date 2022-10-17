from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project',null=True)
    title = models.CharField(max_length=255,null=False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='project/',null=False)

    created_at = models.DateTimeField(auto_now=True)
