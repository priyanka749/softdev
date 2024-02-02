# Generated by Django 5.0 on 2024-01-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_birds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birds',
            name='age',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven')], default=1),
        ),
        migrations.AlterField(
            model_name='birds',
            name='color',
            field=models.CharField(choices=[('black', 'Black'), ('brown', 'Brown'), ('white', 'White'), ('grey', 'Grey'), ('Tabby', 'Tabby')], default='Tabby', max_length=255),
        ),
        migrations.AlterField(
            model_name='birds',
            name='friendliness',
            field=models.CharField(choices=[('Outgoing', 'Outgoing'), ('very social', 'Very Social'), ('Reserved', 'Reserved')], default='Outgoing', max_length=255),
        ),
        migrations.AlterField(
            model_name='birds',
            name='image',
            field=models.ImageField(default='default_image.jpg', max_length=250, null=True, upload_to='pet_images/'),
        ),
        migrations.AlterField(
            model_name='birds',
            name='name',
            field=models.CharField(default='Kitty', max_length=255),
        ),
        migrations.AlterField(
            model_name='birds',
            name='size',
            field=models.CharField(choices=[('10-20 small lbs', 'Small'), ('30-40 lbs medium', 'Medium'), ('50-60 lbs large', 'Large')], default='10-20 small lbs', max_length=255),
        ),
        migrations.AlterField(
            model_name='birds',
            name='species',
            field=models.CharField(choices=[('sparrow', 'Sparrow'), ('parrot', 'Parrot'), ('Cockatiel', 'Cockatiel'), ('Lovebird', 'Lovebird')], default='parrot', max_length=255),
        ),
    ]