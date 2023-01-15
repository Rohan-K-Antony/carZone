from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class carAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f"<img src={object.car_photo.url} width=40 style ='border-radius : 50px'></img>")
    thumbnail.short_description = "Image"
    list_display = ['thumbnail','car_title','city','body_style','color','model','year','is_featured']
    list_display_links = ['thumbnail','car_title']
    search_fields = ['city','car_title','model','color','year']
    list_filter =['year','model','city','body_style']
    list_editable =['is_featured']
admin.site.register(Car,carAdmin)