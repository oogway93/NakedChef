from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Table)
admin.site.register(Hall)
admin.site.register(Order)
admin.site.register(OrderItem)
