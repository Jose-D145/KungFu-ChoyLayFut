from django.urls import path

from .views import EscolaDetailView, EscolaListView

app_name = "escolas"

urlpatterns = [
    path("", EscolaListView.as_view(), name="list"),
    path("<slug:slug>/", EscolaDetailView.as_view(), name="detail"),
    path("estilo/<slug:slug>/", EscolaListView.as_view(), name="list_by_estilo"),
]
