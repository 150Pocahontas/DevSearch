# Generated by Django 4.1.5 on 2023-01-26 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='social_website',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='social_youtube',
        ),
    ]
