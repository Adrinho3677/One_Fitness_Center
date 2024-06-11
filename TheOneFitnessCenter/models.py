from django.db import models
from datetime import datetime

# Create your models here.

class Assinatura(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to = 'fotos/%Y/%m/%d/')
    data = models.DateTimeField(default=datetime.now(), blank=False,)

    def __str__(self):
        return f'nome: {self.nome}, descrição: {self.descricao}, foto: {self.foto}'