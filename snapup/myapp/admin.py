from django.contrib import admin
from .models import Image

# Register your models here.

#to craete table named 'Image' in admin
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_disp=['id','photo','date']

#as we need to deal w imgs we install pillow