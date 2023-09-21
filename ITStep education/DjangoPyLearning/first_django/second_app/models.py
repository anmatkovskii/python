from django.db import models
import base64


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="images/")
    image_base64 = models.CharField(max_length=1000000, blank=True)

    def save(self, *args, **kwargs):
        self.image_base64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}, {self.price}, {self.description}"


class Match(models.Model):
    MatchNumber = models.IntegerField()
    RoundNumber = models.IntegerField()
    DateUtc = models.DateTimeField()
    Location = models.CharField(max_length=100)
    HomeTeam = models.CharField(max_length=100)
    AwayTeam = models.CharField(max_length=100)
    Group = models.CharField(max_length=100, null=True)
    HomeTeamScore = models.IntegerField()
    AwayTeamScore = models.IntegerField()