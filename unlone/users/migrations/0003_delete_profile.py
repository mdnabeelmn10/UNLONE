# Generated by Django 5.1.1 on 2024-12-27 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_age'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
