# Generated by Django 4.0.1 on 2023-02-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0002_product_image_product_image_base64'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MatchNumber', models.IntegerField()),
                ('RoundNumber', models.IntegerField()),
                ('DateUtc', models.DateTimeField()),
                ('Location', models.CharField(max_length=100)),
                ('HomeTeam', models.CharField(max_length=100)),
                ('AwayTeam', models.CharField(max_length=100)),
                ('Group', models.CharField(max_length=100, null=True)),
                ('HomeTeamScore', models.IntegerField()),
                ('AwayTeamScore', models.IntegerField()),
            ],
        ),
    ]
