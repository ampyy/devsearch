# Generated by Django 4.0.6 on 2022-07-27 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_projects_user_alter_skill_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='datetime',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='modified_date',
            field=models.DateField(auto_now=True),
        ),
    ]
