from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    userRank = models.CharField(max_length=50, null=True)
    userTelegramId = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.username}, {self.password}, {self.userRank}'


class Task(models.Model):
    DONE_CHECK = (
        ("Done", "Done"),
        ("In Process", "In Process"),
        ("Expired", "Expired"),
        ("Not Started", "Not Started"),
        ("Cancelled", "Cancelled"),
        ("Declined", "Declined")
    )

    taskName = models.CharField(max_length=100)
    taskDescription = models.TextField(max_length=10000, blank=True, null=True)
    startTime = models.DateTimeField(blank=True, null=True)
    endTime = models.DateTimeField(blank=True, null=True)
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    done = models.CharField(max_length=20, choices=DONE_CHECK, default="Not Started")

    def __str__(self):
        return f'{self.taskName}, {self.startTime}, {self.endTime}, {self.userID}'