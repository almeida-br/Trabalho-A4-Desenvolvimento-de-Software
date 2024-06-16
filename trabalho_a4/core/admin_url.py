
from django.urls import path
from core import views

urlpatterns = [
    path("",views.adminHome, name="admin_home"),
    path("alunos/",views.admin_Alunos, name="admin_alunos"),
    path("adicionar_aluno/",views.admin_AdicionarAluno),
    path("professores/",views.admin_Professores, name="admin_professores"),
    path("disciplinas/",views.admin_Disciplinas, name="admin_disciplinas"),
    path("turmas/",views.admin_Turmas, name="admin_turmas"),
    path("relatorios/",views.admin_Relatorios, name="admin_relatorios")
]