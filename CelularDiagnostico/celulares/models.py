from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, related_name='modelos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
