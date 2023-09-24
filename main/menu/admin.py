from django.contrib import admin
from .models import Menu, Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    fields = ('section',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price')
    fields = (
        ('section', 'title'),
        'the_dish',
        ('price', 'weight'),
        'img')

