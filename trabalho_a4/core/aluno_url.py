
from django.urls import path
from core import views

urlpatterns = [
    path("",views.alunoHome, name="aluno_home"),
    path("quadro_horarios/",views.aluno_Quadro, name="aluno_quadro"),
    path("disciplinas/",views.aluno_Disciplinas, name="aluno_disciplinas"),
]