# Generated by Django 5.0.6 on 2024-07-17 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_userprofile_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='region',
        ),
    ]
