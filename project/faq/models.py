# coding: utf-8

from django.db import models
from django.utils import timezone

class Guardian(models.Model):
    '''Classe que mapeia a tabela Guardian no banco de dados'''

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
        ''' 
        Retorna string que representa um Guardian
        Segue o fomato: LOGIN_GUARDIAN
        '''
        return self.login

class FAQ(models.Model):
    '''Classe que mapeia a tabela FAQ no banco de dados'''

    id_guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    data = models.DateField(blank=True, null=True)
    problema = models.CharField(max_length=255)
    descricao = models.TextField()
    keywords = models.CharField(max_length=100)
    curtidas = models.IntegerField(blank=True, null=True)

    def set_data(self):
        '''Funcao que altera a data da FAQ para a data atual'''
        
        self.data = timezone.now()
        self.save()

    def __str__(self):
        '''
        Retorna string que representa uma FAQ
        Segue o formato: LOGIN_GUARDIAN - ID_FAQ - PROBLEMA
        '''
        return self.id_guardina.login + " - " + str(self.id) + " - " + str(self.problema)

class Solucao(models.Model):
    '''Classe que mapeia a tabela Solucao no banco de dados'''

    id_guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    id_faq = models.ForeignKey(FAQ, on_delete=models.CASCADE)
    data = models.DateField(blank=True, null=True)
    solucao = models.TextField()
    fontes = models.TextField(blank=True, null=True)

    def set_data(self):
        '''Funcao que altera a data da Solucao para a data atual'''

        self.data = timezone.now() 
        self.data = timezone.now()
        self.save()

    def __str__(self):
        '''
        Retorna string que representa uma Solucao
        Segue o formato: LOGIN_GUARDIAN - ID_SOLUCAO - ID_FAQ
        '''
        return self.id_guardian.login + " - " + str(self.id) + " - " + str(self.id_faq.id)

class Pergunta(models.Model):
    '''Classe que mapeia a tabela Pergunta no banco de dados'''

    id_guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    data = models.DateTimeField(blank=True, null=True)
    pergunta = models.CharField(max_length=255)
    descricao = models.TextField()

    def set_data(self):
        '''Funcao que altera a data da Pergunta para a data atual'''
       
        self.data = timezone.now()
        self.save()

    def __str__(self):
        '''
        Retorna string que representa uma Pergunta
        Segue o formato: LOGIN_GUARDIAN - ID_PERGUNTA - PERGUNTA
        '''
        return self.id_guardian.login + " - " + str(self.id) + " - " + self.pergunta

class Resposta(models.Model):
    '''Classe que mapeia a tabela Resposta no banco de dados'''    

    id_guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)
    id_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    resposta = models.TextField()

    def set_data(self):        
        '''Funcao que altera a data da Resposta para a data atual'''

        self.data = timezone.now()
        self.save()

    def __str__(self):
        '''
        Retorna string que representa uma Resposta 
        Segue o formato: LOGIN_GUARDIAN - ID_RESPOSTA - ID_PERGUNTA 
        '''   
        return self.id_guardian.login + " - " + str(self.id) + " - " + str(self.id_pergunta.id)
