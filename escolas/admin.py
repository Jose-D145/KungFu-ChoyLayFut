from django.contrib import admin

from .models import Estilo, Escola


@admin.register(Estilo)
class EstiloAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]


@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "estilo",
        "image",
        "description",
        "fundacao",
        "inclusao",
        "alteracao",
        "is_available",

    ]
    list_filter = ["is_available", "inclusao", "alteracao"]
    list_editable = ["description", "is_available"]



