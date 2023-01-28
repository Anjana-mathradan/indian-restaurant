# Generated by Django 4.1.3 on 2023-01-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_remove_categorydb_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='frontregisterdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Profile')),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
                ('Cpassword', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
