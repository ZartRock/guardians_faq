from django.db import models

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
