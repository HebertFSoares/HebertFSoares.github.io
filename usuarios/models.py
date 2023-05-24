from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    USUARIO_CHOICES = [
        ('estudante', 'Estudante'),
        ('anfitriao', 'Anfitrião'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=USUARIO_CHOICES, null=True, blank=True)
    estado_civil = models.CharField(max_length=50, null=True, blank=True)
    
    # Campos extras para o tipo de usuário "estudante"
    
    cpf_estudante = models.CharField(max_length=14, null=True, blank=True)
    telefone_estudante = models.CharField(max_length=9)
    nome_pai = models.CharField(max_length=100, null=True, blank=True)
    nome_mae = models.CharField(max_length=100, null=True, blank=True)
    instituicao = models.CharField(max_length=100, null=True, blank=True)
    periodo = models.CharField(max_length=50, null=True, blank=True)
    resumo_academico = models.TextField(null=True, blank=True)
    
    # Campos extras para o tipo de usuário "anfitriao"
    
    cpf_anfitriao = models.CharField(max_length=14, null=True, blank=True)
    telefone_anfitriao = models.CharField(max_length=9, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    descricao_espaco = models.TextField(null=True, blank=True)
    comodidades = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.usuario.username
    
