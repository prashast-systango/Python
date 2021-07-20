from django.db import models
from django.db.models.fields import DateTimeField, IntegerField

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    fees = models.IntegerField()

class Teacher(CommonInfo):
    salary = models.IntegerField()

class Constructor(CommonInfo):
    date = DateTimeField()
    payment = IntegerField()