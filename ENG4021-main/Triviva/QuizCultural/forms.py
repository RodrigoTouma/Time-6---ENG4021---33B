from django import forms
from .models import Pergunta


class PerguntaForm(forms.ModelForm):
    """Formulário para criar ou editar perguntas do quiz cultural."""
    class Meta:
        model = Pergunta
        fields = '__all__'
