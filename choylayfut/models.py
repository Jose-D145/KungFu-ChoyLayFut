from django.db import models
from django.contrib.auth.models import User

# models do choylayfut
class Escolas(models.Model):
    nome_escola = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nome_escola
