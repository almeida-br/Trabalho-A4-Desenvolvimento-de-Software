
from django.urls import include, path
from core import views

urlpatterns = [
    path("",views.adminHome, name="admin_home"),
    path("alunos/",views.admin_Alunos, name="admin_alunos"),
    path("professores/",views.admin_Professores, name="admin_professores"),
    path("disciplinas/",views.admin_Disciplinas, name="admin_disciplinas"),
    path("turmas/",views.admin_Turmas, name="admin_turmas"),
    path("relatorios/",include('core.relatorio_url')),
    path("adicionar_aluno/",views.admin_AdicionarAluno, name="adicionar_aluno"),
    path("adicionar_professor/",views.admin_AdicionarProfessor, name="adicionar_professor"),
    path("adicionar_turma/",views.admin_AdicionarTurma, name="adicionar_turma"),
    path("adicionar_disciplina/",views.admin_AdicionarDisciplina, name="adicionar_disciplina"),
    path("adicionar_relatorio/",views.admin_AdicionarRelatorio, name="adicionar_relatorio"),
    path("exibir/",include("core.exibir_url")),
    path("deletar/",include("core.deletar_url"))
]