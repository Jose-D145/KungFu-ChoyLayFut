from django.contrib import admin

from .models import Faixa


@admin.register(Faixa)
class FaixaAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "nivel", "cor_faixa", "created", "modified"]