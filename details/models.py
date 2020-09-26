from django.db import models


# Create your models here.
class Mentor(models.Model):
    mentor = models.CharField(max_length=50, blank=False, default='')
    lecture = models.CharField(max_length=50, blank=False, default='')
    status = models.BooleanField(default=False)
    Remark = models.CharField(max_length=50, blank=False, default='')


class Student(models.Model):
    student = models.CharField(max_length=50, blank=False, default='')
    math = models.CharField(max_length=50, blank=False, default='')
    physics = models.CharField(max_length=50, blank=False, default='')
    english = models.CharField(max_length=50, blank=False, default='')
    status = models.BooleanField(default=False)
    Remark = models.CharField(max_length=50, blank=False, default='')