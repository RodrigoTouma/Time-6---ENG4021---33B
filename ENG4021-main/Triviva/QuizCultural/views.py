from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Pergunta, Alternativa, Pontuacao
from django.db.models import Q
import random
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "index.html")

def modo_nacional(request):
    perguntas = list(Pergunta.objects.filter(origem="nacional"))
    random.shuffle(perguntas)

    # criar sessão do quiz
    request.session["perguntas"] = [p.id for p in perguntas[:10]]
    request.session["index"] = 0
    request.session["pontos"] = 0
    request.session["modo"] = "nacional"

    return HttpResponseRedirect(reverse_lazy("quiz:quiz_pergunta"))

def modo_global(request):
    perguntas = list(Pergunta.objects.filter(origem="global"))
    random.shuffle(perguntas)

    request.session["perguntas"] = [p.id for p in perguntas[:10]]
    request.session["index"] = 0
    request.session["pontos"] = 0
    request.session["modo"] = "global"

    return HttpResponseRedirect(reverse_lazy("quiz:quiz_pergunta"))

def modo_ranqueado(request):
    perguntas = list(Pergunta.objects.all())
    random.shuffle(perguntas)

    request.session["perguntas"] = [p.id for p in perguntas[:15]]
    request.session["index"] = 0
    request.session["pontos"] = 0
    request.session["modo"] = "ranqueado"

    return HttpResponseRedirect(reverse_lazy("quiz:quiz_pergunta"))

def modo_relogio(request):
    perguntas = list(Pergunta.objects.all())
    random.shuffle(perguntas)

    request.session["perguntas"] = [p.id for p in perguntas[:10]]
    request.session["index"] = 0
    request.session["pontos"] = 0
    request.session["modo"] = "relogio"

    return HttpResponseRedirect(reverse_lazy("quiz:quiz_pergunta"))

def quiz_pergunta(request):
    perguntas = request.session.get("perguntas", [])
    index = request.session.get("index", 0)

    # acabou o quiz
    if index >= len(perguntas):
        return HttpResponseRedirect(reverse_lazy("quiz:resultado"))

    pergunta_id = perguntas[index]
    pergunta = Pergunta.objects.get(id=pergunta_id)
    alternativas = pergunta.alternativas.all()

    contexto = {
        "pergunta": pergunta,
        "alternativas": alternativas,
        "numero": index + 1,
        "total": len(perguntas)
    }

    return render(request, "quiz_pergunta.html", contexto)


def responder(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse_lazy("quiz:quiz_pergunta"))

    alternativa_id = request.POST.get("alternativa")
    alternativa = Alternativa.objects.get(id=alternativa_id)

    # Soma ponto se correta
    if alternativa.correta:
        request.session["pontos"] = request.session.get("pontos", 0) + 1

    # Avança pergunta
    request.session["index"] = request.session.get("index", 0) + 1

    return HttpResponseRedirect(reverse_lazy("quiz:quiz_pergunta"))


def resultado(request):
    pontos = request.session.get("pontos", 0)
    modo = request.session.get("modo", "")

    # salva ranking se for modo ranqueado
    if modo == "ranqueado" and request.user.is_authenticated:
        Pontuacao.objects.create(usuario=request.user, pontos=pontos)

    contexto = {"pontos": pontos, "modo": modo}

    return render(request, "resultado.html", contexto)


def ranking(request):
    ranking = Pontuacao.objects.all()
    return render(request, "ranking.html", {"ranking": ranking})
