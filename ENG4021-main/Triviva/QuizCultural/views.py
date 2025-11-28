from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Pergunta
from django.db.models import Q
import random

def home(request):
    return render(request, "index.html")

def modo_nacional(request):
    if request.method == 'GET':
        # If the request method is GET, render the form
        perguntas = list(Pergunta.objects.filter(origem="nacional"))
        random.shuffle(perguntas)
        contexto = {"perguntas": perguntas}
        return render(request, "modo-nacional.html", contexto)
    else:
        return HttpResponseRedirect(reverse_lazy("quiz:home"))

def modo_global(request):
    if request.method == "GET":
        perguntas = list(Pergunta.objects.filter(origem="global"))
        random.shuffle(perguntas)
        contexto = {"perguntas": perguntas}
        return render(request, "modo-global.html", contexto)
    else:
        return HttpResponseRedirect(reverse_lazy("quiz:home"))

def modo_ranqueado(request):
    if request.method == "GET":
        perguntas = list(Pergunta.objects.filter(Q(origem="nacional") | Q(origem="global")))
        random.shuffle(perguntas)
        contexto = {"perguntas": perguntas}
        return render(request, "modo-ranqueado.html", contexto)
    else:
        return HttpResponseRedirect(reverse_lazy("quiz:home"))

def modo_relogio(request):
    if request.method == "GET":
        perguntas = list(Pergunta.objects.filter(Q(origem="nacional") | Q(origem="global")))
        random.shuffle(perguntas)
        contexto = {"perguntas": perguntas,"tempo_limite": 60}
        return render(request, "modo-relogio.html", contexto)
    else:
        return HttpResponseRedirect(reverse_lazy("quiz:home"))