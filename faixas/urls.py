from django.urls import path

from .views import FaixaDetailView, FaixaListView

app_name = "faixas"

urlpatterns = [
    path("", FaixaListView.as_view(), name="list"),
    path("<slug:slug>/", FaixaDetailView.as_view(), name="detail"),

]