from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        'id', 'created',
        ('first_name', 'last_name'),
        'email',
        ('hall', 'place'),
        'status', 'initiator',
    )
    readonly_fields = ('id', 'created', 'initiator')

