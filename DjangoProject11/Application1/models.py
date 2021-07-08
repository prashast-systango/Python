from django.db import models

# Create your models here.
class Student(models.Model):
    StuId = models.IntegerField()
    StuName = models.CharField(max_length = 30)
    StuEmail = models.EmailField(max_length = 20)
    StuPass = models.CharField(max_length = 20)