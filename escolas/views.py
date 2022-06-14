from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Estilo, Escola


class EscolaDetailView(DetailView):
    queryset = Escola.available.all()


class EscolaListView(ListView):
    estilo = None

    def get_queryset(self):
        queryset = Escola.available.all()

        estilo_slug = self.kwargs.get("slug")
        if estilo_slug:
            self.estilo = get_object_or_404(Estilo, slug=estilo_slug)
            queryset = queryset.filter(estilo=self.estilo)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estilo"] = self.estilo
        context["estilos"] = Estilo.objects.all()
        return context
