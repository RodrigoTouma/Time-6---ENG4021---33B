from django.urls import path
from . import views

app_name = 'quizcultural'

urlpatterns = [
    # Página inicial do quiz cultural
    path('', views.home, name='home'),
    # Lista todas as perguntas cadastradas
    path('lista/', views.listar_perguntas, name='listar_perguntas'),
    # Formulário de busca
    path('busca/', views.busca, name='busca'),
    # Resultado da busca
    path('resultado/', views.resultado_busca, name='resultado_busca'),
]
