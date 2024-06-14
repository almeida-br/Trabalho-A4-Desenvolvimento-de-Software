from django.db import models

# Create your models here.
class AccessType(models.TextChoices):
    ADMIN = "admi"
    ALUNO = "alun"
    PROFESSOR = "prof"

class Login(models.Model):
    id=models.IntegerField(primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=4,choices=AccessType.choices)

class Professor(models.Model):
    nome=models.CharField(max_length=50)

class Disciplina(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    professores=models.ManyToManyField(Professor)
    conteudo=[models.FileField]
    cargaHoraria=models.IntegerField()
    horario=models.DateField()

class Aluno(models.Model):
    matricula=models.IntegerField(primary_key=True)
    cpf=models.IntegerField()
    nome=models.CharField(max_length=200)
    endereco=models.CharField(max_length=400)
    telefone=models.IntegerField()
    dataAdmissao=models.DateField(auto_now_add=True)
    turmaCod=models.IntegerField()
    disciplinas=models.ManyToManyField(Disciplina)
    login=models.ForeignKey(Login,on_delete=models.CASCADE,default=("00","null","null","n/a"))
