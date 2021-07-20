from django.contrib import admin
from django.db import models
from .models import Student, Teacher, Constructor

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'fees']
    
    

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'salary']


@admin.register(Constructor)
class ConstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'payment']
