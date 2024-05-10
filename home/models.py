from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200),
    email = models.EmailField( max_length=254),
    phone = models.CharField(max_length=12),
    desc = models.TextField(),
    date = models.DateField()
