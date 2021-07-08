from django.db import models

class Student(models.Model):
    Stu_id = models.IntegerField(primary_key = True)
    Stu_name = models.CharField(max_length = 20)