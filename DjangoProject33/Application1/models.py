from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    roll_no = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=50)
    