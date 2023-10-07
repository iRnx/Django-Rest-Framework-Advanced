from django.contrib import admin
from usuarios.models import Usuario
from django.contrib.auth.admin import UserAdmin


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'id')
    list_display_links = ('email',)
    