from django.contrib import admin
from .models.contact import Contact
from user.models.project import Project_Message


class ContactAdmin(admin.ModelAdmin):
    search_fields=('name',)
    list_display=['name','email','date','message']
    list_filter =['date']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Project_Message)
