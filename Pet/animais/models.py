from django.db import models
from django.contrib .auth.models import User

# Create your models here.
class Animais(models.Model):
    TIPO = [
        ('CACHORRO', 'CACHORRO'),
        ('GATO', 'GATO')
    ]

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    Tipo = models.CharField(max_length=8, choices=TIPO)
    Nome = models.CharField(max_length=45)
    Raça = models.CharField(max_length=45)
    Porte = models.CharField(max_length=50)
    Cor = models.CharField(max_length=120)
    Descrição = models.CharField(max_length=300)
    Foto_1 = models.URLField(null=True)
    Foto_2 = models.URLField(null=True)
    Foto_3 = models.URLField(null=True)
    Foto_4 = models.URLField(null=True)
    Foto_5 = models.URLField(null=True)

    def __str__(self):
        return f'{self.Nome} {self.Tipo}'
from django.db import models

# Create your models here.
