# from django.db import models

# # Create your models here.
# class author(models.Model):
#     id=models.AutoField(primary_key=True,db_column='ID')
#     name=models.CharField(max_length=200,null=False)
#     publishdate=models.DateTimeField(auto_now_add=True)
#     updatedate=models.DateTimeField(auto_now=True)
#     image=models.CharField(max_length=200,null=True)
#     version=models.IntegerField()
from django.db import models
from django.utils import timezone
from author.models import *
class Author(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=200, null=False)
    publishdate = models.DateTimeField(auto_now_add=True)  # Only use auto_now_add
    updatedate = models.DateTimeField(auto_now=True)  # Only use auto_now
    image = models.CharField(max_length=200, null=True, blank=True)  # Remove default=timezone.now
    version = models.IntegerField(default=1)  # Provide a default value
authorobj = models.ForeignKey("author.Author", on_delete=models.CASCADE, null=True, blank=True)
