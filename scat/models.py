from django.db import models
from datetime import datetime

# Create your models here.


class Cliente(models.Model):

    cnpjcli = models.CharField(
        max_length=14, primary_key=True, null=False, blank=False)
    razcli = models.CharField(max_length=40, null=False, blank=False)
    contatocli = models.CharField(max_length=20)
    telcli = models.CharField(max_length=14)
    ramalcli = models.CharField(max_length=5)
    celcli = models.CharField(max_length=15)
    endcli = models.CharField(max_length=30)
    bairrocli = models.CharField(max_length=20)
    ufcli = models.CharField(max_length=2)
    cepcli = models.CharField(max_length=9)


class Tecnico(models.Model):
    cpftec = models.CharField(
        max_length=11, primary_key=True, null=False, blank=False)
    nometec = models.CharField(max_length=30, null=False, blank=False)
    celtec = models.CharField(max_length=15)
    funtec = models.CharField(max_length=15)


class Atividades(models.Model):
    nomeativ = models.CharField(max_length=20)


class Agenda(models.Model):
    acnpjcli = models.ForeignKey(
        Cliente, max_length=14, on_delete=models.CASCADE)
    acpftec = models.ForeignKey(
        Tecnico, max_length=11, on_delete=models.CASCADE)
    aidativ = models.ForeignKey(
        Atividades, max_length=int, on_delete=models.CASCADE)
    dataserv = models.DateField(null=False, blank=False)
    datacri = models.DateField(default=datetime.now, blank=True)
