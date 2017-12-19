from django.contrib import admin
from main.models import(
    Category, News, Review)

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Review)

