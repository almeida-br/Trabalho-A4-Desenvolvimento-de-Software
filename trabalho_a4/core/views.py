import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from core.models import *


# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'pages/login.html')
    else:
        username=request.POST.get('login')
    
        login=Login.objects.get(login=username).getAccess()
        if login=="admin":
            return redirect('/admin/')
        elif login=="aluno":
            return redirect('/aluno/')
        elif login=="professor":
            return redirect('/professor/')
        else:
            return render(request,'index.html',context={"type":login})
        

def recuperaSenha(request):
    if request.method=='GET':
        return render(request,'pages/recupera_senha.html')
    else:
        matricula=request.POST.get('matricula')
        email=request.POST.get('email')
        login=Login.objects.get(login=email)
        if login:
            return render(request,'pages/recupera_senha_2.html')
        else:
            return render(request,'pages/recupera_senha.html')
    

#def redirect(request):
#    if request.method=='GET':
#        return render(request,'pages/index.html')
#    else:
#        username=request.POST.get('login')
#        password=request.POST.get('senha')
    
#        login=Login.objects.get(login=username).getAccess()
#        return render(request,'admin_home.html',context={"type":login})
        

#páginas Admin
def adminHome(request):
    return render(request,'pages/admin_home.html')

def admin_Alunos(request):
 
    return render(request,'pages/admin_alunos.html')

def admin_AdicionarAluno(request):
    if request.method=='GET':
        return render(request,'pages/admin_adicionarAluno.html')
    else:
        matricula=request.POST.get("matricula")
        cpf=request.POST.get("cpf")
        nome=request.POST.get("nome")
        telefone=request.POST.get("telefone")
        data=request.POST.get("data")
        turma=request.POST.get("turma")


        endereco=Endereco(id=random.randint(1,99999999),
                    logradouro=request.POST.get("end_logradouro"),
                    numero=request.POST.get("end_numero"),
                    bairro=request.POST.get("end_bairro"),
                    uf=request.POST.get("end_uf"),
                )
        login=Login(id=random.randint(1,99999999),login=matricula+"@utopia.br",password="UTOPIA@"+data, access="aluno")

        aluno=Aluno(
            matricula,
            cpf,
            nome,
            endereco=endereco,
            telefone=telefone,
            dataAdmissao=data,
            turmaCod=turma,
            login=login
        )
        aluno.save()
        Aluno.objects.create(aluno)
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
