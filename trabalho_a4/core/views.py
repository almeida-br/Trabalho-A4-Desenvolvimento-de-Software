import random
from django.template.loader import render_to_string
from django.http import FileResponse, HttpResponse
from django.shortcuts import render,redirect
from prompt_toolkit import HTML
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
    return render(request,'pages/admin/admin_home.html')


def exibirAluno(request,id):
    aluno=Aluno.objects.get(matricula=id)

    context={
        'aluno':aluno,
    }
    return render(request,"pages/admin/exibir/exibir_aluno.html",context)

def exibirProfessor(request,id):
    professor=Professor.objects.get(matricula=id)
    context={
        'professor':professor
    }
    return render(request,"pages/admin/exibir/exibir_professor.html",context)

def exibirDisciplina(request,id):
    context={
        'disciplina':Disciplina.objects.get(codigo=id)
    }
    return render(request,"pages/admin/exibir/exibir_disciplina.html",context)

def exibirTurma(request,id):
    context={
        'turma':Turma.objects.get(codigo=id)
    }
    return render(request,"pages/admin/exibir/exibir_turma.html",context)

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
      
    return render(request,'pages/admin/adicionar/admin_adicionarAluno.html', {'alunoForm': alunoForm})

def admin_AdicionarProfessor(request):
    if request.method=="POST":

        professorForm=ProfessorForm(request.POST,prefix='professor')
        if professorForm.is_valid():
            professorForm.save(commit=True)
            return redirect('/admin/professores/')
    
    else:
        professorForm=ProfessorForm(prefix='professor')
    return render(request,'pages/admin/adicionar/admin_adicionarProfessor.html', {'professorForm': professorForm})

def admin_AdicionarTurma(request):
    if request.method=="POST":

        turmaForm=TurmaForm(request.POST,prefix='turma')
        if turmaForm.is_valid():
            turmaForm.save(commit=True)
            return redirect('/admin/turmas/')
    
    else:
        turmaForm=TurmaForm(prefix='turma')
    return render(request,'pages/admin/adicionar/admin_adicionarTurma.html', {'turmaForm': turmaForm})

def admin_AdicionarDisciplina(request):
    if request.method=="POST":

        disciplinaForm=DisciplinaForm(request.POST,prefix='disciplina')
        if disciplinaForm.is_valid():
            disciplinaForm.save(commit=True)
            return redirect('/admin/disciplinas/')
    
    else:
        disciplinaForm=DisciplinaForm(prefix='disciplina')
    return render(request,'pages/admin/adicionar/admin_adicionarDisciplina.html', {'disciplinaForm': disciplinaForm})

def admin_AdicionarRelatorio(request):
  
    return render(request,'pages/admin/adicionar/admin_adicionarRelatorio.html')


def alunoRelatorio(request):
    # Fetch the data you want to export
    alunos = Aluno.objects.all()

    # Render the HTML content
    html_content = render_to_string('pages/pdf_template.html', {'alunos': alunos})

    # Convert HTML to PDF
    pdf = HTML(string=html_content).write_pdf()

    # Return the PDF as a response
    return FileResponse(pdf, as_attachment=True, filename='export.pdf')

def professorRelatorio(request):
    # Fetch the data you want to export
    professores = Professor.objects.all()

    # Render the HTML content
    html_content = render_to_string('pages/pdf_template.html', {'professores': professores})

    # Convert HTML to PDF
    pdf = HTML(string=html_content).write_pdf()

    # Return the PDF as a response
    return FileResponse(pdf, as_attachment=True, filename='export.pdf')

def disciplinaRelatorio(request):
    # Fetch the data you want to export
    disciplinas = Disciplina.objects.all()

    # Render the HTML content
    html_content = render_to_string('pages/pdf_template.html', {'disciplinas': disciplinas})

    # Convert HTML to PDF
    pdf = HTML(string=html_content).write_pdf()

    # Return the PDF as a response
    return FileResponse(pdf, as_attachment=True, filename='export.pdf')

def turmaRelatorio(request):
    # Fetch the data you want to export
    turmas = Turma.objects.all()

    # Render the HTML content
    html_content = render_to_string('pages/pdf_template.html', {'turmas': turmas})

    # Convert HTML to PDF
    pdf = HTML(string=html_content).write_pdf()

    # Return the PDF as a response
    return FileResponse(pdf, as_attachment=True, filename='export.pdf')


def admin_Alunos(request):
    alunos=Aluno.objects.all().values()
    context = {
    'alunos': alunos,
    }
    return render(request,'pages/admin/admin_alunos.html',context)


def admin_Professores(request):
    professores=Professor.objects.all().values()
    context = {
    'professores': professores,
    }
    return render(request,'pages/admin/admin_professores.html',context)

def admin_Disciplinas(request):
    disciplinas=Disciplina.objects.all().values()
    context = {
    'disciplinas': disciplinas,
    }
    return render(request,'pages/admin/admin_disciplinas.html',context)

def admin_Turmas(request):
    turmas=Turma.objects.all().values()
    context = {
    'turmas': turmas
    }
    return render(request,'pages/admin/admin_turmas.html',context)

def admin_Relatorios(request):
    return render(request,'pages/admin/admin_relatorios.html')

#páginas Aluno

def alunoHome(request):
    return render(request,'pages/aluno/aluno_home.html')

def aluno_Quadro(request):
    return render(request,'pages/aluno/aluno_quadro_horarios.html')

def aluno_Disciplinas(request):
    return render(request,'pages/aluno/aluno_disciplinas.html')

def aluno_Solicitacoes(request):
    return render(request,'pages/aluno/aluno_solicitacoes.html')

#páginas Professor

def professorHome(request):
    return render(request,'pages/professor/professor_home.html')

def professor_Turmas(request):
    return render(request,'pages/professor/professor_turmas.html')

def professor_Disciplinas(request):
    return render(request,'pages/professor/professor_disciplinas.html')

def professor_Solicitacoes(request):
    return render(request,'pages/professor/professor_solicitacoes.html')
