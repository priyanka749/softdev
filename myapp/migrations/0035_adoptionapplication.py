# Generated by Django 5.0 on 2024-02-02 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_rename_dogbreed_dogadoption_breed'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=255)),
                ('breed', models.CharField(max_length=255)),
                ('experience', models.TextField()),
                ('reason_for_adoption', models.TextField()),
            ],
        ),
    ]
