# Generated by Django 5.2 on 2025-04-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='literarycharacter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='character_images/'),
        ),
    ]
