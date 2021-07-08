from django.db import models

class Student(models.Model):
    StuId = models.IntegerField()
    StuName = models.CharField(max_length = 30)
    StuEmail = models.EmailField(max_length = 20)
    StuPass = models.CharField(max_length = 20)

    def __str__(self):
        return self.StuName