from typing import OrderedDict
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ordem')


class Faixa(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    nivel = models.CharField(max_length=50, null=False)
    cor_faixa = models.ImageField(upload_to="faixas/%Y/%m/%d", blank=True)
    ordem = models.IntegerField(null=False, default=0)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    objects = models.Manager()
    available = AvailableManager()
    
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name




