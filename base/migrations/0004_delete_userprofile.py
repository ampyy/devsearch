# Generated by Django 4.0.6 on 2022-07-17 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
