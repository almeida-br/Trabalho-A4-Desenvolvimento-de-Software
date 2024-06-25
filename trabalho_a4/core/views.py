import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from core.models import *


# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'pages/login.html')
    else:
        username=request.POST.get('login')
    
        login=Login.objects.get(login=username).access
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


def exibirAluno(request,id):
    aluno=Aluno.objects.get(matricula=id)

    context={
        'aluno':aluno,
    }
    return render(request,"exibir_aluno.html",context)

def exibirProfessor(request,id):
    professor=Professor.objects.get(matricula=id)
    context={
        'professor':professor
    }
    return render(request,"exibir_professor.html",context)

def exibirDisciplina(request,id):
    context={
        'disciplina':Disciplina.objects.get(codigo=id)
    }
    return render(request,"exibir_disciplina.html",context)

def exibirTurma(request,id):
    context={
        'turma':Turma.objects.get(codigo=id)
    }
    return render(request,"exibir_turma.html",context)

def deleteAluno(request,matricula):
    Aluno.objects.get(matricula=matricula).delete()
    
    return redirect('/admin/alunos/')

def deleteProfessor(request,id):
    Professor.objects.get(matricula=id).delete()
    return redirect('/admin/professores/')

def deleteDisciplina(request,id):
    Disciplina.objects.get(codigo=id).delete()
    return redirect('/admin/discicplinas/')

def deleteTurma(request,id):
    Turma.objects.get(codigo=id).delete()
    return redirect('/admin/turmas/')


def admin_AdicionarAluno(request):
    if request.method=="POST":

        alunoForm=AlunoForm(request.POST,prefix='aluno')

        if alunoForm.is_valid():
            alunoForm.save()

            return redirect('/admin/alunos/')
    
    else:
        alunoForm=AlunoForm(prefix='aluno')
      
    return render(request,'pages/admin_adicionarAluno.html', {'alunoForm': alunoForm})

def admin_AdicionarProfessor(request):
    if request.method=="POST":

        professorForm=ProfessorForm(request.POST,prefix='professor')
        if professorForm.is_valid():
            professorForm.save(commit=True)
            return redirect('/admin/professores/')
    
    else:
        professorForm=ProfessorForm(prefix='professor')
    return render(request,'pages/admin_adicionarProfessor.html', {'professorForm': professorForm})

def admin_AdicionarTurma(request):
    if request.method=="POST":

        turmaForm=TurmaForm(request.POST,prefix='turma')
        if turmaForm.is_valid():
            turmaForm.save(commit=True)
            return redirect('/admin/turmas/')
    
    else:
        turmaForm=TurmaForm(prefix='turma')
    return render(request,'pages/admin_adicionarTurma.html', {'turmaForm': turmaForm})

def admin_AdicionarDisciplina(request):
    if request.method=="POST":

        disciplinaForm=DisciplinaForm(request.POST,prefix='disciplina')
        if disciplinaForm.is_valid():
            disciplinaForm.save(commit=True)
            return redirect('/admin/disciplinas/')
    
    else:
        disciplinaForm=DisciplinaForm(prefix='disciplina')
    return render(request,'pages/admin_adicionarDisciplina.html', {'disciplinaForm': disciplinaForm})

def admin_AdicionarRelatorio(request):
  
    return render(request,'pages/admin_adicionarRelatorio.html')


def admin_Alunos(request):
    alunos=Aluno.objects.all().values()
    context = {
    'alunos': alunos,
    }
    return render(request,'pages/admin_alunos.html',context)


def admin_Professores(request):
    professores=Professor.objects.all().values()
    context = {
    'professores': professores,
    }
    return render(request,'pages/admin_professores.html',context)

def admin_Disciplinas(request):
    disciplinas=Disciplina.objects.all().values()
    context = {
    'disciplinas': disciplinas,
    }
    return render(request,'pages/admin_disciplinas.html',context)

def admin_Turmas(request):
    turmas=Turma.objects.all().values()
    context = {
    'turmas': turmas
    }
    return render(request,'pages/admin_turmas.html',context)

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
