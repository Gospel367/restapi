from django.contrib import admin
from . models import Category, MyDictionary, Project


class MyDictionaryAdmin(admin.ModelAdmin):
    list_display = ['words', 'type']
    search_fields = ['words',]

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(MyDictionary, MyDictionaryAdmin)