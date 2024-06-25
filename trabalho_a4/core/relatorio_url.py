
from django.urls import include, path
from core import views

urlpatterns = [
    path("",views.admin_Relatorios, name="relatorio_home"),
    path("alunos/",views.alunoRelatorio),
    path("professores/",views.professorRelatorio),
    path("disciplinas/",views.disciplinaRelatorio),
    path("turmas/",views.turmaRelatorio),
    
]