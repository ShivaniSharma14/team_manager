from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Resource(models.Model):
    title       = models.CharField(max_length=50)
    description = models.TextField()
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
