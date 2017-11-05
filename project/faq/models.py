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
        return self.problema
