# Generated by Django 3.2.10 on 2024-01-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_id_animal_pet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='pet_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
