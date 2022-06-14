from django.contrib import admin

from .models import Caminho


@admin.register(Caminho)
class CaminhoAdmin(admin.ModelAdmin):
    list_display = ["faixa", "atividade", "slug", "objetivo", "detalhe", "sequencia", "ativo"]



