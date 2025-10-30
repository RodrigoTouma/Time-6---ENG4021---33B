from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Pergunta


def home(request):
    """Renderiza a página inicial do Quiz Cultural."""
    return render(request, 'quizcultural/home.html')


@login_required
def listar_perguntas(request):
    """Exibe todas as perguntas cadastradas no banco de dados."""
    perguntas = Pergunta.objects.all()
    contexto = {'perguntas': perguntas}
    return render(request, 'quizcultural/lista.html', contexto)


@login_required
def busca(request):
    """Exibe um formulário simples para buscar perguntas por texto."""
    return render(request, 'quizcultural/busca.html')


@login_required
def resultado_busca(request):
    """Filtra perguntas contendo o termo de busca enviado via GET."""
    termo = request.GET.get('termo', '')
    if termo:
        perguntas = Pergunta.objects.filter(texto__icontains=termo)
    else:
        perguntas = Pergunta.objects.all()
    contexto = {'perguntas': perguntas, 'busca': termo}
    return render(request, 'quizcultural/lista.html', contexto)
