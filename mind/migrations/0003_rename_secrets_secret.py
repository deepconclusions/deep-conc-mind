# Generated by Django 4.2.6 on 2023-10-15 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mind', '0002_secrets'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Secrets',
            new_name='Secret',
        ),
    ]
