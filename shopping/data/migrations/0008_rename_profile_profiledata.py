# Generated by Django 4.0 on 2022-01-07 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_profile_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profile',
            new_name='profiledata',
        ),
    ]
