# Generated by Django 5.0 on 2024-02-02 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_rename_country_dogadoption_pet_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogadoption',
            old_name='dogBreed',
            new_name='Breed',
        ),
    ]
