from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dishes')
    cost = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def quantity_validator(value):
    if value == 0:
        raise ValueError('Количество должно быть больше нуля')


class Basket(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='baskets')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='baskets')
    quantity = models.PositiveIntegerField(validators=[quantity_validator])

    def __str__(self):
        return self.dish.name


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.create_date)


class ElementOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='elements')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='elements')
    quantity = models.PositiveIntegerField(validators=[quantity_validator])

    def __str__(self):
        return self.dish.name
