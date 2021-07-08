from django.contrib import admin
from Application1.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('StuId', 'StuName', 'StuEmail')

# admin.site.register(Student ,StudentAdmin)