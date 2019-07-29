from django.db import models
from colorfield.fields import ColorField
from faicon.fields import FAIconField

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)   
    icon = FAIconField()
    bg_color = ColorField(default='#ffffff')  

    def __str__(self):
        return self.title