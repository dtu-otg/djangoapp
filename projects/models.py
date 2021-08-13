from django.db import models
from user.models import User,Profile
from django.utils.translation import gettext_lazy as _


def upload_to(instance,filename):
    return 'projects/{filename}'.format(filename=filename)

class Project(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length = 300,null = True,blank=True)
    image = models.ImageField(_("Image"),upload_to=upload_to,default='events/default.jpeg')
    discord = models.CharField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return self.name + " Project"
    