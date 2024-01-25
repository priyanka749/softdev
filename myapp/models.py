from django.forms import ValidationError
from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import ImageField

class User_profile(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

from django.db import models



# models.py
from django.db import models

class Animal_dog(models.Model):
    BREED_CHOICES = [

        ('German Shepherd', 'German Shepherd'),
        ('Bulldog', 'Bulldog'),
        ('French Bulldog', 'French Bulldog'),
        ('Golden Retriever', 'Golden Retriever'),
        ('Chow Chow', 'Chow Chow'),
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
    ]

    BEHAVIOR_CHOICES = [
        ('Digging', 'Digging'),
        ('Eating Poop', 'Eating Poop'),
        ('Head Pressing', 'Head Pressing'),
        ('Scooting', 'Scooting'),
        ('Yawning', 'Yawning'),
        ('Biting', 'Biting'),
        ('Circling', 'Circling'),
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
        ('10-20 small lbs', '1 Queen Pillow'),
        ('30-40 lbs medium', '2 Standard Pillows'),
        ('50-60 lbs large', '2 King Pillows'),
        ('70-80 lbs xl', '3 King Pillows'),
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
    dog_Description = models.CharField(max_length=1000,default='')
    dog_History = models.CharField(max_length=1000,default='Sorry we do not have much history on this dog.')
    
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
    cat_Description = models.CharField(max_length=1000,default='')
    cat_History = models.CharField(max_length=1000,default='Sorry we do not have much history on this dog.')
    def __str__(self):
        return self.name


from django.db import models

class Birds(models.Model):
    COLOR_CHOICES = [
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('white', 'White'),
        ('grey', 'Grey'),
        ('Tabby', 'Tabby'),
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

    SPECIES_CHOICES = [
        ('sparrow', 'Sparrow'),
        ('parrot', 'Parrot'),
        ('Cockatiel', 'Cockatiel'),
        ('Lovebird', 'Lovebird'),
    ]

    SIZE_CHOICES = [
        ('10-20 small lbs', 'Small'),
        ('30-40 lbs medium', 'Medium'),
        ('50-60 lbs large', 'Large'),
    ]

    FRIENDLINESS_CHOICES = [
        ('Outgoing', 'Outgoing'),
        ('very social', 'Very Social'),
        ('Reserved', 'Reserved'),
    ]

    bird_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='Bird')
    color = models.CharField(max_length=255, default='Grey', choices=COLOR_CHOICES)
    age = models.IntegerField(default=1, choices=AGE_CHOICES)
    species = models.CharField(max_length=255, default='parrot', choices=SPECIES_CHOICES)
    size = models.CharField(max_length=255, default='10-20 small lbs', choices=SIZE_CHOICES)
    friendliness = models.CharField(max_length=255, default='Outgoing', choices=FRIENDLINESS_CHOICES)
    image = models.ImageField(upload_to='pet_images/', max_length=250, null=True, default='default_image.jpg')
    bird_Description = models.CharField(max_length=1000,default='')
    bird_History = models.CharField(max_length=1000,default='Sorry we do not have much history on this dog.')

    def __str__(self):
        return self.name


class other_animals(models.Model):
    animal_id=models.AutoField(primary_key=True)
    animal= models.CharField(max_length=100)
    age=models.IntegerField(default=1)
    about_it= models.TextField()
    image = models.ImageField(upload_to='pet_images/', max_length=250, null=True, default='default_image.jpg')

    animal_Description = models.CharField(max_length=1000,default='')
    animal_History = models.CharField(max_length=1000,default='Sorry we do not have much history on this Animal.')
    about_species = models.CharField(max_length=1000,default='specific')
    
    def __str__(self):
        return self.animal


class Donation_data(models.Model):
    donate_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.ImageField(upload_to='donation_images/', null=True, blank=True)

  
    def __str__(self):
        return f"Donation #{self.donate_id} - {self.full_name}"


class DogAdoption(models.Model):
    
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    EXPERIENCE_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('experienced', 'Experienced'),
    )

    name = models.CharField(max_length=10,default="hari")
    email = models.EmailField()
    telephone = models.CharField(max_length=20,default="9852182125")
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    
    petname = models.CharField(max_length=10,)
    petgender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dogBreed = models.CharField(max_length=100)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    reason_for_adoption = models.TextField()

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name    
from django.db import models


