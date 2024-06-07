from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def adminHome(request):
    return render(request,'core/admin.html')

def alunoHome(request):
    return render(request,'core/aluno.html')

def professorHome(request):
    return render(request,'core/professor.html')