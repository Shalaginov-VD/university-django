# Generated by Django 5.1.6 on 2025-02-16 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Groups',
            new_name='Group',
        ),
        migrations.RenameModel(
            old_name='Stundents',
            new_name='Stundent',
        ),
    ]
