from django.db import models
from rest_framework.fields import _UnvalidatedField
from user.models import User,Profile
from django.utils.translation import gettext_lazy as _

class Course(models.Model):
    '''
        islab = True/False
        group = G1/G2/G3
    '''
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=10, null=True)
    islab = models.BooleanField(null=True, blank=True, default=False)
    group = models.CharField(max_length=2, null=True, blank=True)
    batch = models.CharField(max_length=9, null=True)
    prof_name = models.CharField(max_length=100, null=True, blank=True)
    prof_mail = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.code + ": " + self.name + " " + self.batch + (" LAB" if self.islab else "")


class Slot(models.Model):
    '''
        day = MON, TUE, ...
        time = 1100, 1600, etc
        duration = 1/2/3
    '''
    day = models.CharField(max_length=3)
    time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.day + ", " + str(self.time)

