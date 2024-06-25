
from django.urls import include, path
from core import views

urlpatterns = [  
    path("aluno/<int:matricula>/",views.deleteAluno),
    path("professor/<int:matricula>/",views.deleteProfessor),
    path("disciplina/<str:id>/",views.deleteDisciplina),
    path("turma/<str:id>/",views.deleteTurma),
]