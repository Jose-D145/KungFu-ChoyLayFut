from django.urls import path

from .views import CaminhoListView

app_name = "caminhos"

urlpatterns = [
    path("", CaminhoListView.as_view(), name="list"),

]