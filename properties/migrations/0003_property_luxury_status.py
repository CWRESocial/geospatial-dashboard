# Generated by Django 5.0.1 on 2025-07-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_alter_property_latitude_alter_property_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='luxury_status',
            field=models.CharField(choices=[('luxurious', 'Luxurious'), ('non_luxurious', 'Non-Luxurious')], default='non_luxurious', max_length=20),
        ),
    ]
