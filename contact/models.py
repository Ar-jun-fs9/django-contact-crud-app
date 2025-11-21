from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=50)                 # Short text for username
    email = models.EmailField(max_length=122, unique=True)     # EmailField validates email format
    phone = models.CharField(max_length=10, unique=True)                    # Store 10-digit phone as string
    password = models.CharField(max_length=128)   


    def __str__(self):
        return self.username
