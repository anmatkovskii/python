# Generated by Django 4.0.1 on 2023-02-04 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_doctorsexamination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateTimeField()),
                ('DepartmentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.departments')),
                ('SponsorID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.sponsor')),
            ],
        ),
    ]