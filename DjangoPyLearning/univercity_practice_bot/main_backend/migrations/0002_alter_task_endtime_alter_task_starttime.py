# Generated by Django 4.0.1 on 2023-02-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='endTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='startTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
