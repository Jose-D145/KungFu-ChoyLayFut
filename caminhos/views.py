from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Caminho


class CaminhoListView(ListView):

    def get_queryset(self):
        queryset = Caminho.available.all()

        return queryset
