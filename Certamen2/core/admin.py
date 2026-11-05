from django.contrib import admin
from .models import Categoria, LugarPatrimonial

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    ordering = ['nombre']

class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'ubicacion', 'anio_construccion', 'categoria']
    ordering = ['nombre']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(LugarPatrimonial, LugarPatrimonialAdmin)