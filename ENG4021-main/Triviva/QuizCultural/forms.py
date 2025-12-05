from django import forms
from .models import Pergunta

class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = "__all__"
