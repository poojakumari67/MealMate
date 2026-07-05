from django.contrib import admin

from .models import Cart, Customer, Restaurant, Item

# Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Cart)
