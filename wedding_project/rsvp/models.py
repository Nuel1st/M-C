from django.db import models

# Create your models here.

class RSVP(models.Model):
    name =  models.CharField(max_length=100)
    email = models.EmailField()
    attending =  models.BooleanField(default=False)
    guests = models.IntegerField(default=0)


    def __str__(self):
        return self.name
