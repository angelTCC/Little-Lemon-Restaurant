from django.contrib import admin

# Register your models here.
from .models import MenuItem
from .models import Category

admin.site.register(MenuItem)
admin.site.register(Category)