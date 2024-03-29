# Generated by Django 5.0 on 2024-01-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_user_delete_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
