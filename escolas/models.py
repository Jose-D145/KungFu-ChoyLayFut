from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Estilo(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "estilo"
        verbose_name_plural = "estilos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("escolas:list_by_estilo", kwargs={"slug": self.slug})


class Escola(TimeStampedModel):
    estilo = models.ForeignKey(
        Estilo, related_name="escolas", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="escolas/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    fundacao = models.DateTimeField(auto_now=True)
    inclusao = models.DateTimeField(auto_now_add=True)
    alteracao = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("escolas:detail", kwargs={"slug": self.slug})

