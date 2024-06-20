from django.shortcuts import render
from .forms import LoginForm


# Create your views here.

def recuperaSenha(request):
    return render(request,'pages/recupera_senha.html')


#páginas Admin
def adminHome(request):
    return render(request,'pages/admin_home.html')

def admin_Alunos(request):
    return render(request,'pages/admin_alunos.html')

def admin_AdicionarAluno(request):

    return render(request,'pages/admin_adicionarAluno.html')

def admin_Professores(request):
    return render(request,'pages/admin_professores.html')

def admin_Disciplinas(request):
    return render(request,'pages/admin_disciplinas.html')

def admin_Turmas(request):
    return render(request,'pages/admin_turmas.html')

def admin_Relatorios(request):
    return render(request,'pages/admin_relatorios.html')

#páginas Aluno
def alunoHome(request):
    return render(request,'pages/aluno_home.html')

def aluno_Quadro(request):
    return render(request,'pages/aluno_quadro_horarios.html')

def aluno_Disciplinas(request):
    return render(request,'pages/aluno_disciplinas.html')

def aluno_Solicitacoes(request):
    return render(request,'pages/aluno_solicitacoes.html')

#páginas Professor
def professorHome(request):
    return render(request,'pages/professor_home.html')

def professor_Turmas(request):
    return render(request,'pages/professor_turmas.html')

def professor_Disciplinas(request):
    return render(request,'pages/professor_disciplinas.html')

def professor_Solicitacoes(request):
    return render(request,'pages/professor_solicitacoes.html')
