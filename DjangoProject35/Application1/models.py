from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=40)
    marks = models.IntegerField()
    pass_date = models.DateField()
    admdatetime = models.DateTimeField()
    