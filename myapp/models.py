from django.forms import ValidationError
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import ImageField

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
    # timestamp = models.DateTimeField(auto_now_add=True)

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


# models.py


# models.py
from django.db import models

class Animal_dog(models.Model):
    BREED_CHOICES = [

        ('German Shepherd', 'German Shepherd'),
        ('Bulldog', 'Bulldog'),
        ('French Bulldog', 'French Bulldog'),
        ('Golden Retriever', 'Golden Retriever'),
        ('Chow Chow', 'Chow Chow'),
        # Add more breeds as needed
    ]

    COLOR_CHOICES = [
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('white', 'White'),
        ('grey', 'Grey'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('gold', 'Gold'),
        ('cream', 'Cream'),
        # Add more colors as needed
    ]

    BEHAVIOR_CHOICES = [
        ('Digging', 'Digging'),
        ('Eating Poop', 'Eating Poop'),
        ('Head Pressing', 'Head Pressing'),
        ('Scooting', 'Scooting'),
        ('Yawning', 'Yawning'),
        ('Biting', 'Biting'),
        ('Circling', 'Circling'),
        # Add more behaviors as needed
    ]

    AGE_CHOICES = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
        (6, 'Six'),
        (7, 'Seven'),
        # Add more age options as needed
    ]

    SIZE_CHOICES = [
        ('10-20 small lbs', '1 Queen Pillow'),
        ('30-40 lbs medium', '2 Standard Pillows'),
        ('50-60 lbs large', '2 King Pillows'),
        ('70-80 lbs xl', '3 King Pillows'),
        # Add more size options as needed
    ]

    pet_id = models.AutoField(primary_key=True)
    
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,default='pet')
    breed = models.CharField(max_length=255, default='streetdog', choices=BREED_CHOICES)
    color = models.CharField(max_length=255, default='kalo',choices=COLOR_CHOICES)
    behavior = models.CharField(max_length=255,default='default_behavior',choices=BEHAVIOR_CHOICES,)
    age = models.IntegerField(default='default_behavior', choices=AGE_CHOICES)
    weight = models.CharField(max_length=255, default='default_behavior', choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='animal_images/', default='default_image.jpg')
    def __str__(self):
        return self.name

class Cats(models.Model):

    COLOR_CHOICES = [
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('white', 'White'),
        ('grey', 'Grey'),
        ('tabby', 'tabby'),
        ('Calico', 'Calico'),
    ]

    Friendliness_options = [
        ('Outgoing', 'Outgoing'),
        ('very social', 'very social'),
        ('Reserved', 'Reserved'),
    ]

    AGE_CHOICES = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
        (6, 'Six'),
        (7, 'Seven'),
    ]

    SIZE_CHOICES = [
        ('10-20 small lbs', 'Small'),
        ('30-40 lbs medium', 'Medium'),
        ('50-60 lbs large', 'large'),     
    ]

    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,default='kitty')
    color = models.CharField(max_length=255, default='Tabby',choices=COLOR_CHOICES)
    age = models.IntegerField(default='Unknown', choices=AGE_CHOICES)
    weight = models.CharField(max_length=255, default='default_behavior', choices=SIZE_CHOICES)
    Friendliness=models.CharField(max_length=255, default='medium', choices=Friendliness_options)
    image = models.ImageField(upload_to='animal_images/', max_length=250,null=True,default='default_image.jpg')
    def __str__(self):
        return self.name

