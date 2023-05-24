from django.db import models


class VagaCasa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    regras_casa = models.TextField()
    informacoes_familia = models.TextField()
    contato = models.EmailField()

    def __str__(self):
        return self.titulo
