from django.contrib import admin
from .models import Categoria, Pergunta, Alternativa, Pontuacao

admin.site.register(Categoria)
admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Pontuacao)
