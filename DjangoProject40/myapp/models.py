from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    ##
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    ##
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    ## we can delete the user, but its relationships will not be deleted 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=40)
    post_cat = models.CharField(max_length=40)
    post_publish_date = models.DateField()
