from django.db import models
from celulares.models import Marca, Modelo
from usuarios.models import Usuario

class Diagnostico(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    esta_ligando = models.BooleanField()
    liga_vibra_som_sem_imagem = models.BooleanField()
    liga_sem_carregar = models.BooleanField()
    conector_quebrado = models.BooleanField()
    tela_quebrada = models.BooleanField()
    tampa_traseira_quebrada = models.BooleanField()
    esta_mudo = models.BooleanField()

class Reparo(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, related_name='reparos')
    passo = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='reparos/', blank=True, null=True)
