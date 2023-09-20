from django.db import models

#to create table to database
class Task(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    discription=models.CharField(max_length=500, null=True, blank=True)
