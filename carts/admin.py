from django.contrib import admin
from store.models import Product
from . models import Cart, CartItem

admin.site.register(Cart)
admin.site.register(CartItem)