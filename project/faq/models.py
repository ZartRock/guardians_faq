# coding: utf-8

from django.db import models
from django.utils import timezone

class Guardian(models.Model):
    STATUS_CHOICES = (
        ("ativo", "ativo"),
        ("desativo", "desativo"),
    )

    login = models.CharField(max_length=45, unique=True)
    senha = models.CharField(max_length=45)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ativo")

    def __str__(self):
        return self.login

class FAQ(models.Model):
    id_guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    data = models.DateField(blank=True, null=True)
    problema = models.CharField(max_length=255)
    descricao = models.TextField()
    keywords = models.CharField(max_length=100)
    curtidas = models.IntegerField(blank=True, null=True)

    def set_data(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.id_guardina.login + " - " + str(self.id) + " - " + str(self.problema)

class Solucao(models.Model):
    id_guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    id_faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    data = models.DateField(blank=True, null=True)
    solucao = models.TextField()
    fontes = models.TextField(blank=True, null=True)

    def set_data(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.id_guardian.login + " - " + str(self.id) + " - " + str(self.id_faq.id)

class Pergunta(models.Model):
    id_guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    data = models.DateTimeField(blank=True, null=True)
    pergunta = models.CharField(max_length=255)
    descricao = models.TextField()

    def set_data(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.id_guardian.login + " - " + str(self.id) + " - " + self.pergunta

class Resposta(models.Model):
    id_guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    id_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    resposta = models.TextField()

    def set_data(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.id_guardian.login + " - " + str(self.id) + " - " + str(self.id_pergunta.id)
