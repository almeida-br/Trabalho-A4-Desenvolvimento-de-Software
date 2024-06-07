from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)

class Professor(models.Model):
    nome=models.CharField(max_length=50)

class Disciplina(models.Model):
    codigo=models.IntegerField()
    nome = models.CharField(max_length=100)
    professores=models.ManyToManyField(Professor)
    conteudo=[models.FileField]
    cargaHoraria=models.IntegerField()
    horario=models.DateField()

class Aluno(models.Model):
    matricula=models.IntegerField()
    cpf=models.IntegerField()
    nome=models.CharField(max_length=200)
    endereco=models.CharField(max_length=400)
    telefone=models.IntegerField()
    dataAdmissao=models.DateField()
    turmaCod=models.IntegerField()
    disciplinas=models.ManyToManyField(Disciplina)
    #login=models.OneToOneField(Login)
