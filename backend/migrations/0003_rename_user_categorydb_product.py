# Generated by Django 4.1.3 on 2022-11-26 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_categorydb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorydb',
            old_name='User',
            new_name='Product',
        ),
    ]
