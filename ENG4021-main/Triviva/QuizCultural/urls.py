from django.urls.conf import path
from QuizCultural import views

app_name = "QuizCultural"

urlpatterns = [
    path("home/", views.home, name='homepage'),
    path("insereCarro/", views.insereCarro, name='insereCarro'),
]
