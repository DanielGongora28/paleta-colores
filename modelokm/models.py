from django.db import models

# Create your models here.
class color_pal(models.Model):
    img = models.ImageField()
    palette= models.CharField(max_length=200)