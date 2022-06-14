from typing import OrderedDict
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from faixas.models import Faixa


class Caminho(models.Model):
    faixa = models.ForeignKey(Faixa, on_delete=models.PROTECT)
    atividade = models.CharField(max_length=255, null=False)
    objetivo = models.CharField(max_length=255)
    detalhe = models.TextField(blank=True)
    sequencia = models.IntegerField(null=False, default=0)
    ativo = models.BooleanField(default=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="atividade")

    objects = models.Manager()

    
    class Meta:
        ordering = ("faixa", "sequencia",)

    def __str__(self):
        return self.atividade
