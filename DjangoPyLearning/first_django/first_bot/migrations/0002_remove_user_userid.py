# Generated by Django 4.0.1 on 2023-02-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userID',
        ),
    ]