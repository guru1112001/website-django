from pyexpat import model
from django.db import models

# Create your models here.
class blogs(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    update_at=models.DateField(auto_now=True)
    author=models.CharField(max_length=50)
    Views=models.IntegerField()
    likes=models.IntegerField()