from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200, default="John Doe")  # Default name
    email = models.EmailField(max_length=254, default="example@example.com")  # Default email
    phone = models.CharField(max_length=12, default="1234567890")  # Default phone number
    desc = models.TextField(default="")  # Default description
    date = models.DateField(auto_now_add=True)  # Default date (current date/time when object is created)
