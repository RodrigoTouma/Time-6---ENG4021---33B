from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.home, name='homepage'),
    path("nacional/", views.modo_nacional, name='modo_nacional'),
    path("global/", views.modo_global, name='modo_global'),
    path("ranqueado/", views.modo_ranqueado, name='modo_ranqueado'),
    path("relogio/", views.modo_relogio, name='modo_relogio'),
]
