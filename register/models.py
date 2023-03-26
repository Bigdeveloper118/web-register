from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.IntegerField(null=True)
    joined_name = models.DateField(null=True)