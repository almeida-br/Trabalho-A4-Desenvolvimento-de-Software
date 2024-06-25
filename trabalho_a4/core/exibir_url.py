
from django.urls import include, path
from core import views

urlpatterns = [
    #path("",views.adminHome, name="admin_home"),
    path("aluno/<str:id>/",views.exibirAluno, name="exibir_aluno"),
    path("professor/<str:id>/",views.exibirProfessor, name="exibir_professor"),
    path("disciplina/<str:id>/",views.exibirDisciplina, name="exibir_disciplina"),
    path("turma/<str:id>/",views.exibirTurma, name="exibir_turma"),
    path("relatorio/",views.admin_Relatorios, name="admin_relatorios"),
    
]