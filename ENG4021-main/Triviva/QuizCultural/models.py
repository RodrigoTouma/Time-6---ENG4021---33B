from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_meta_plural = "Categorias"

    def __str__(self):
        return self.nome

class Pergunta(models.Model):
    enunciado = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="perguntas")
    dificuldade=models.CharField(max_length=20,default="normal",choices=[("facil","Fácil"),("normal","Normal"),("dificil","Difícil")])

class Meta:
    verbose_name = "Pergunta"
    verbose_name_plural = "Perguntas"

def __str__(self):