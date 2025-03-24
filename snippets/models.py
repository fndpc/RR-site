from django.db import models

# Create your models here.
class Snipet(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    photo =  models.ImageField()
    

    def __str__(self):
        return self.title