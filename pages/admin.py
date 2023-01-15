from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html(f"<img src={object.profile_pic.url} width=40 style ='border-radius : 50px'></img>")
    thumbnail.short_description = "Photo"
    list_display =['id','thumbnail','first_name','last_name','designation','created_date']
    search_fields =['first_name','last_name','designation']
    list_filter =['designation']
    list_display_links=['thumbnail']

admin.site.register(models.Team,TeamAdmin)