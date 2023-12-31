# Generated by Django 4.0.1 on 2023-02-04 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_disease_doctor_examination_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endTime', models.TimeField()),
                ('startTime', models.TimeField()),
                ('doctorID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.doctor')),
                ('examinationID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.examination')),
                ('wardID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.ward')),
            ],
        ),
    ]
