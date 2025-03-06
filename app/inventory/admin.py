from django.contrib import admin
from .models import Computer, Printer, Accessory

admin.site.register(Computer)
admin.site.register(Printer)
admin.site.register(Accessory)