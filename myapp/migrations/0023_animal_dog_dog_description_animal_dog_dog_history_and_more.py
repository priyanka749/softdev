# Generated by Django 5.0 on 2024-01-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_dogadoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal_dog',
            name='dog_Description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='animal_dog',
            name='dog_History',
            field=models.CharField(default='Sorry we do not have much history on this dog.', max_length=1000),
        ),
        migrations.AddField(
            model_name='birds',
            name='bird_Description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='birds',
            name='bird_History',
            field=models.CharField(default='Sorry we do not have much history on this dog.', max_length=1000),
        ),
        migrations.AddField(
            model_name='cats',
            name='cat_Description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='cats',
            name='cat_History',
            field=models.CharField(default='Sorry we do not have much history on this dog.', max_length=1000),
        ),
        migrations.AddField(
            model_name='donation_data',
            name='about_species',
            field=models.CharField(default='specific', max_length=1000),
        ),
        migrations.AddField(
            model_name='donation_data',
            name='animal_Description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='donation_data',
            name='animal_History',
            field=models.CharField(default='Sorry we do not have much history on this Animal.', max_length=1000),
        ),
    ]
