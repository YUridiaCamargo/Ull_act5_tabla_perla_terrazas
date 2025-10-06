from django.contrib import admin

# Register your models here.
from .models import producto
#registrar eñ modelo producto en el admin
admin.site.register(producto)
