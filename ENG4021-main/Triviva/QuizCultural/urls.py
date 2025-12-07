from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.home, name='homepage'),

    path("modo/nacional/", views.pagina_modo_nacional, name="pagina_modo_nacional"),
    path("modo/global/", views.pagina_modo_global, name="pagina_modo_global"),
    path("modo/ranqueado/", views.pagina_modo_ranqueado, name="pagina_modo_ranqueado"),
    path("modo/relogio/", views.pagina_modo_relogio, name="pagina_modo_relogio"),

    path("iniciar/nacional/", views.iniciar_nacional, name="iniciar_nacional"),
    path("iniciar/global/", views.iniciar_global, name="iniciar_global"),
    path("iniciar/ranqueado/", views.iniciar_ranqueado, name="iniciar_ranqueado"),
    path("iniciar/relogio/", views.iniciar_relogio, name="iniciar_relogio"),

    path("pergunta/", views.quiz_pergunta, name="quiz_pergunta"),
    path("responder/", views.responder, name="responder"),
    path("resultado/", views.resultado, name="resultado"),
    path("ranking/", views.ranking, name="ranking"),
]
