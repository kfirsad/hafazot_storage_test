from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'copy_link', 'publish_date', 'description', 'file')



admin.site.unregister(Group)
admin.site.register(Item, ItemAdmin)
