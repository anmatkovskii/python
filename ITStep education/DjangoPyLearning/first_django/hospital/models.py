from django.core.exceptions import ValidationError
from django.db import models


class Departments(models.Model):
    NUMBERS = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )

    id = models.AutoField(primary_key=True)
    building = models.IntegerField(choices=NUMBERS)
    financing = models.IntegerField()
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}, {self.building}, {self.financing}'


class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    severity = models.IntegerField(default=1)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}, {self.severity}'


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100, unique=True)
    salary = models.IntegerField()
    surname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.phone}, {self.salary}'


class Examination(models.Model):
    NUMBERS = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7")
    )

    id = models.AutoField(primary_key=True)
    DayOfWeek = models.IntegerField(choices=NUMBERS)
    EndTime = models.DateTimeField()
    name = models.CharField(max_length=100, unique=True)
    StartTime = models.DateTimeField()

    def clean(self):
        if self.StartTime > self.EndTime:
            raise ValidationError('Error, StartTime is bigger than EndTime')

    def __str__(self):
        return f'{self.name}, {self.DayOfWeek}, {self.StartTime}, {self.EndTime}'


class Ward(models.Model):
    NUMBERS = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )

    id = models.AutoField(primary_key=True)
    building = models.IntegerField(choices=NUMBERS)
    floor = models.IntegerField()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.name}, {self.floor}, {self.building}'


class DoctorsExamination(models.Model):
    endTime = models.TimeField()
    startTime = models.TimeField()
    doctorID = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    examinationID = models.ForeignKey(Examination, on_delete=models.SET_NULL, null=True)
    wardID = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True)

    def clean(self):
        if self.startTime > self.endTime:
            raise ValidationError('Error, StartTime is bigger than EndTime')


class Sponsor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField()
    DepartmentID = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    SponsorID = models.ForeignKey(Sponsor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.amount}, {self.date}, {self.DepartmentID}, {self.SponsorID}'


