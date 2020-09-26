from django.db import models


# Create your models here.
class Details(models.Model):
    Mentor_Name = models.CharField(max_length=50,blank=False, default='')
    Student_Name = models.CharField(max_length=50, blank=False, default='')
    Status = models.CharField(max_length=50, blank=False, default='')
    Remark = models.CharField(max_length=50, blank=False, default='')