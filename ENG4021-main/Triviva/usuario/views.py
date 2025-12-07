from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


@login_required
def paginaSecreta(request):
    return render(request, 'seguranca/paginaSecreta.html')


class ClasseProtegida(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chatsec/inicio.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'chatsec/inicio.html')


def cadastro(request):
    if request.method == "POST":

        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        senha1 = request.POST.get("senha1")
        senha2 = request.POST.get("senha2")

        # 1. Verifica senha
        if senha1 != senha2:
            messages.error(request, "As senhas não coincidem!")
            return render(request, "usuario/cadastro.html")

        # 2. Verifica email já existente
        if User.objects.filter(username=email).exists():
            messages.error(request, "Este email já está cadastrado.")
            return render(request, "usuario/cadastro.html")

        # 3. Criar usuário
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=senha1
        )

        user.save()

        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect("login")

    return render(request, "usuario/cadastro.html")
