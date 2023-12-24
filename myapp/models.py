from ckeditor.fields import RichTextField
from django.db import models


class User(models.Model):
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    # image = models.ImageField()

    def __str__(self):
        return self.user_id
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"