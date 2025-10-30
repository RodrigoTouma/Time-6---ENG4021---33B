from django.db import models


class Pergunta(models.Model):
    """
    Modelo que representa uma pergunta do quiz cultural.
    Cada pergunta possui um texto e quatro alternativas (A, B, C e D), além da
    indicação de qual alternativa é a correta, categoria e nível de dificuldade.
    """
    texto = models.CharField(max_length=255, help_text='Texto da pergunta')
    opcao_a = models.CharField(max_length=100, help_text='Alternativa A')
    opcao_b = models.CharField(max_length=100, help_text='Alternativa B')
    opcao_c = models.CharField(max_length=100, help_text='Alternativa C')
    opcao_d = models.CharField(max_length=100, help_text='Alternativa D')
    resposta_correta = models.CharField(
        max_length=1,
        help_text='Letra da alternativa correta (A, B, C ou D)'
    )
    categoria = models.CharField(
        max_length=100,
        blank=True,
        help_text='Categoria da pergunta (opcional)'
    )
    dificuldade = models.CharField(
        max_length=50,
        blank=True,
        help_text='Nível de dificuldade (opcional)'
    )

    def __str__(self) -> str:
        return self.texto
