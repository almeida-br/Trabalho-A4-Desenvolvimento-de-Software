from django import forms

from .models import Aluno,Endereco

class AlunoForm(forms.ModelForm):
    class Meta:
        model= Aluno
        fields=('matricula','cpf','nome','endereco','telefone','turmaCod','login')