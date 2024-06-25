from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from core.models import *

class LoginForm(AuthenticationForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
      
class loginView(LoginView):
    template_name="login.html"
    authentication_form = LoginForm 

class AlunoForm(forms.ModelForm):
    class Meta:
        model=Aluno
        fields={"matricula","cpf","nome","telefone","turmaCod","dataAdmissao"}
    
    matricula=forms.CharField(widget=forms.TextInput(attrs={'background': '#F6F6F6','border-radius': '10px','margin-bottom': '26px','padding': '12px 15px 7px 15px'}))
    cpf=forms.CharField(widget=forms.TextInput(attrs={'background': '#F6F6F6','border-radius': '10px','margin-bottom': '26px','padding': '12px 15px 7px 15px'}))
    nome=forms.CharField(widget=forms.TextInput(attrs={'background': '#F6F6F6','border-radius': '10px','margin-bottom': '26px','padding': '12px 15px 7px 15px'}))
    telefone=forms.CharField(widget=forms.TextInput(attrs={'background': '#F6F6F6','border-radius': '10px','margin-bottom': '26px','padding': '12px 15px 7px 15px'}))
    turmaCod=forms.CharField(label="Código da turma",widget=forms.TextInput(attrs={'background': '#F6F6F6','border-radius': '10px','margin-bottom': '26px','padding': '12px 15px 7px 15px'}))
    dataAdmissao=forms.DateField(label="Data de admissão",widget=forms.DateInput(attrs={'background': '#F6F6F6','border-radius': '10px','margin-bottom': '26px','padding': '12px 15px 7px 15px'}))
    field_order=[matricula,cpf,nome,telefone,turmaCod,dataAdmissao]
    

class ProfessorForm(forms.ModelForm):
    class Meta:
        model=Professor
        fields={"matricula","cpf","nome","telefone","nivelEscolaridade","formacao","dataContratacao"}

    matricula=forms.CharField()
    cpf=forms.CharField()
    nome=forms.CharField()
    telefone=forms.CharField()
    nivelEscolaridade=forms.CharField(label="Nivel de escolaridade")
    formacao=forms.CharField()
    dataContratacao=forms.DateField(label="Data de contratação")
    field_order=[matricula,cpf,nome,telefone,nivelEscolaridade,formacao,dataContratacao]


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model=Disciplina
        fields={"codigo","nome","professores","cargaHoraria","horario"}

    codigo=forms.CharField(max_length=8)
    nome=forms.CharField()
    professores=forms.CharField()
    cargaHoraria=forms.CharField(label="Carga horária")
    horario=forms.CharField()

    field_order=[codigo,nome,professores,cargaHoraria,horario]


class TurmaForm(forms.ModelForm):
    class Meta:
        model=Turma
        fields={"codigo","periodo","sala","dataAbertura","quantidadeAlunos"}

    codigo=forms.CharField()
    periodo=forms.CharField()
    sala=forms.CharField()
    dataAbertura=forms.CharField(label="Data de abertura")
    quantidadeAlunos=forms.CharField(label="Quantidade de alunos")

    field_order=[codigo,periodo,sala,dataAbertura,quantidadeAlunos]




