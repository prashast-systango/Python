from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    # models.OneToOneField(to,)

    ## when we delete a user its relationships will also get deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    ## we cannot delete a user which is having a relationship
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    
    ## Limiting the users to make relationships
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})
    
    page_name = models.CharField(max_length=50)
    page_cat = models.CharField(max_length=50)
    page_publish_date = models.DateField()

