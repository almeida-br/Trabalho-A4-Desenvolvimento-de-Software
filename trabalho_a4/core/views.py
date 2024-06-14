from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')



def adminHome(request):
    return render(request,'pages/admin_home.html')

def alunoHome(request):
    return render(request,'pages/aluno_home.html')

def professorHome(request):
    return render(request,'pages/professor_home.html')

def admin_Alunos(request):
    return render(request,'pages/admin_alunos.html')

def admin_Professores(request):
    return render(request,'pages/admin_professores.html')

