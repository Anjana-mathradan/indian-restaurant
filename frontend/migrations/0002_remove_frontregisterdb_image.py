# Generated by Django 4.1.3 on 2023-01-11 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontregisterdb',
            name='Image',
        ),
    ]
