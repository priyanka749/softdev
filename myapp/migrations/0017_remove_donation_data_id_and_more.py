# Generated by Django 5.0 on 2024-01-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_donation_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='donation_data',
            name='donate_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
