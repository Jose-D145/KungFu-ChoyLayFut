from django.views.generic import DetailView, ListView

from models import Escolas


class EscolasListView(ListView):
    model = Escolas


class EscolasDetailView(DetailView):
    model = Escolas
    


