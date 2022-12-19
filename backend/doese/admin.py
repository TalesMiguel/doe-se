from django.contrib import admin
from .models import Instituicoes, User, Acoes

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'user')

class AcoesAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'endereco')

class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'senha')

admin.site.register(Instituicoes, InstituicaoAdmin)

admin.site.register(User, UserAdmin)

admin.site.register(Acoes, AcoesAdmin)
