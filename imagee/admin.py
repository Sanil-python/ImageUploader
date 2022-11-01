from django.contrib import admin
from .models import ImageUpload

# Register your models here.

@admin.register(ImageUpload)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']