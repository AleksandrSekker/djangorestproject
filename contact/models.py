from django.db import models

# Create your models here.
class Contact(models.Model):
    contact = models.CharField(max_length=200)
    def __str__(self):
        return self.contact