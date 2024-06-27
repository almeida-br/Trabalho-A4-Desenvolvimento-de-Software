
from django.urls import path
from core import views

urlpatterns = [
    path("",views.professorHome, name="professor_home"),
    path("turmas/",views.professor_Turmas, name="professor_turmas"),
    path("disciplinas/",views.professor_Disciplinas, name="professor_disciplinas"),
]