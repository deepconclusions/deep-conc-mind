# Generated by Django 4.2.6 on 2023-10-15 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mind', '0003_rename_secrets_secret'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='message',
            new_name='human',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='response',
            new_name='mind_bot',
        ),
    ]
