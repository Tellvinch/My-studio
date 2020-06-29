from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Images, Category, Location


class ImageAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "pub_date", "location", "category"]
    class Meta:
        model = Images

admin.site.register(Images, ImageAdmin )
admin.site.register(Category)
admin.site.register(Location)