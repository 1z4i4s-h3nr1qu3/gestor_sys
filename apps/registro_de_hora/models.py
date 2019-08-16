from django.db import models
from apps.funcionario.models import Funcionarios


class registroHora(models.Model):
    motivo = models.CharField(max_length=100)
    funcionarios = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo