from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    ORIGEM_CHOICES = [("nacional", "Nacional"),("global", "Global")]
    enunciado = models.TextField()
    origem = models.CharField(max_length=20, choices=ORIGEM_CHOICES, default="nacional")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="perguntas")
    dificuldade = models.CharField(max_length=20,default="normal",choices=[("facil", "Fácil"),("normal", "Normal"),("dificil", "Difícil")])

    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"

    def __str__(self):
        return self.enunciado[:50] + "..."

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name="alternativas")
    texto = models.CharField(max_length=255)
    correta = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"

    def __str__(self):
        return f"{self.texto} ({'correta' if self.correta else 'errada'})"

class Pontuacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pontos = models.IntegerField(default=0)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pontuação"
        verbose_name_plural = "Pontuações"
        ordering = ["-pontos", "-data"]

    def __str__(self):
        return f"{self.usuario.username} - {self.pontos} pontos"