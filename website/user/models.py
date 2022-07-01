from django.db import models

class user(models.Model):
    password=models.CharField
    phone_no=models.IntegerField()
    email=models.EmailField()
    

