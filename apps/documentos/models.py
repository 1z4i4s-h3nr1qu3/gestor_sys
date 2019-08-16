from django.db import models
from apps.funcionario.models import Funcionarios


class Documentos(models.Model):
    descricao = models.CharField(max_length=100)
    titular = models.ForeignKey(Funcionarios,
                                on_delete=models.PROTECT)
    def __str__(self):
        return self.descricao
