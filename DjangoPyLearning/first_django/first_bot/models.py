from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}, {self.price}"


class User(models.Model):
    UserID = models.CharField(max_length=50)
    Ballance = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.UserID}, {self.Ballance}"


class Orders(models.Model):
    BuyerID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ProductName = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
