from django.contrib import admin
from TheOneFitnessCenter.models import Assinatura

# Register your models here.

class ConfigProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    list_filter = ('nome',)
    list_per_page = (5)
    search_fields = ('nome',)

admin.site.register(Assinatura, ConfigProdutos)