from django.contrib import admin
from .models import Dish,Order,ElementOrder,Basket,Category
# Register your models here.
list_models = [
    Dish,
    Order,
    ElementOrder,
    Basket,
    Category
]

admin.site.register(list_models)