from django.db import models
from django.contrib .auth.models import User

# Create your models here.
class Contato(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=45)
    Sobrenome = models.CharField(max_length=45)
    Data_de_nascimento = models.CharField(max_length=50)
    Rua = models.CharField(max_length=120)
    Numero = models.CharField(max_length=45)
    Bairro = models.CharField(max_length=45)
    Cidade = models.CharField(max_length=45)
    Celular = models.CharField(max_length=45)
    Foto_Perfil = models.URLField(null=True)

    def __str__(self):
        return f'{self.Nome} {self.Sobrenome}'
