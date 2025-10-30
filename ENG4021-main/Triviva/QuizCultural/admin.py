from django.contrib import admin
from .models import Pergunta


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    """Administração da classe Pergunta no painel do Django."""
    list_display = ("texto", "categoria", "dificuldade")
    search_fields = ("texto", "categoria")
