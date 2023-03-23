from django.contrib import admin
from .models import Profile, CartItems, Cart

# Register your models here.
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItems)
