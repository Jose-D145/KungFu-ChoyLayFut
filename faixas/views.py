from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Faixa


class FaixaDetailView(DetailView):
    queryset = Faixa.available.all()


class FaixaListView(ListView):

    def get_queryset(self):
        queryset = Faixa.available.all()

        return queryset

