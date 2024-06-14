
from django.urls import path
from core import views

urlpatterns = [
    path("",views.adminHome, name="admin_home"),
    path("alunos/",views.admin_Alunos, name="admin_alunos"),
    path("professores/",views.admin_Professores, name="admin_professores")
]