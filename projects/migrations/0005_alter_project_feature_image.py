# Generated by Django 4.1.5 on 2023-01-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='feature_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]