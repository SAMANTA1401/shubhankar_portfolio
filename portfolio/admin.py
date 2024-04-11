from django.contrib import admin
from .models import *

# Register your models here.
class Contactlist(admin.ModelAdmin):
    list_display = ['name','email','phonenumber','description']
    search_fields = ['name','email']
    list_filter = ['name','email','phonenumber','description']
admin.site.register(Contact, Contactlist)

admin.site.register(Blogs)
