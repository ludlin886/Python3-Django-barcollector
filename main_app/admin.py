from django.contrib import admin

from .models import Bar, Rating, Available

admin.site.register(Bar)

admin.site.register(Rating)

admin.site.register(Available)