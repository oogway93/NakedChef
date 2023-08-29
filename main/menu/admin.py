from django.contrib import admin
from .models import Menu, Section


class ActionAdmin(admin.ModelAdmin):
    fields = ('section',)


class MenuAdmin(admin.ModelAdmin):
    fields = ('section', 'title')


admin.site.register(Section)
admin.site.register(Menu)
