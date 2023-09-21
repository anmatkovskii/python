from django.db import models
import base64


class ProductGrocery(models.Model):
    TYPE_CHOICE = (
        ("FRUIT", "Fruit"),
        ("VEGETABLE", "Vegetable")
    )

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    type = models.CharField(max_length=100, choices=TYPE_CHOICE)
    image = models.ImageField(upload_to="images/")
    image_base64 = models.CharField(max_length=1000000, blank=True)

    def save(self, *args, **kwargs):
        self.image_base64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(ProductGrocery, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}, {self.price}, {self.description}"


