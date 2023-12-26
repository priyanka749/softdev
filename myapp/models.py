from django.forms import ValidationError
from ckeditor.fields import RichTextField
from django.db import models


class User(models.Model):
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    # image = models.ImageField()
from django.db import models
import re

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # def clean(self):
    #     super().clean()
    #     self.validate_telephone()
    #     self.validate_email()

    # def validate_telephone(self):
    #     if not re.match(r'^\d{10}$', self.telephone):
    #         raise ValidationError("Telephone number should be 10 digits long.")

    # def validate_email(self):
    #     if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email):
    #         raise ValidationError("Enter a valid email address.")
