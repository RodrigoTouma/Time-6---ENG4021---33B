from django.shortcuts import render
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