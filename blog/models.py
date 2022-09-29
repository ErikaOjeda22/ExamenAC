from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    dato1=models.FloatField(blank=True, null=True)
    dato2=models.CharField(max_length=10)
    dato3=models.FloatField(blank=True, null=True)
    dato4=models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.dato1)+','+str(self.dato2)+','+str(self.dato3)+','+str(self.dato4)