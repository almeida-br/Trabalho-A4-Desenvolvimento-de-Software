from django.db import models

# Create your models here.
class AccessType(models.TextChoices):
    ADMIN = "admin"
    ALUNO = "aluno"
    PROFESSOR = "professor"

class Professor(models.Model):
    matricula=models.IntegerField(primary_key=True,default=0000000000)
    cpf=models.BigIntegerField(default=00000000000)
    nome=models.CharField(max_length=50)
    telefone=models.CharField(max_length=11,default=00000000000)
    cursosMinistrados=[models.CharField]
    nivelEscolaridade=models.CharField
    formacao=[models.CharField]
    dataContratacao=models.DateField
    disciplinasMinistradas=[models.CharField]
   
class Disciplina(models.Model):
    codigo=models.IntegerField(primary_key=True,default=0)
    nome = models.CharField(max_length=100)
    professores=models.ManyToManyField(Professor)
    conteudo=[models.FileField]
    cargaHoraria=models.IntegerField(default=0)
    horario=models.DateField()

class Aluno(models.Model):
    matricula=models.IntegerField(primary_key=True,default=0000000000)
    cpf=models.BigIntegerField(default=00000000000)
    nome=models.CharField(max_length=200)
    telefone=models.CharField(max_length=11,default=00000000000)
    dataAdmissao=models.DateField()
    turmaCod=models.CharField(max_length=8)
    disciplinas=models.ManyToManyField(Disciplina)


class Turma(models.Model):
    codigo=models.CharField(max_length=8,primary_key=True)
    periodo=models.IntegerField(default=0)
    sala=models.CharField(max_length=20)
    dataAbertura=models.DateField()
    quantidadeAlunos=models.IntegerField(default=0)

class Login(models.Model):
    id=models.OneToOneField(Aluno or Professor,primary_key=True,on_delete=models.CASCADE)
    login=models.EmailField()
    password=models.CharField(max_length=50)
    access=models.CharField(max_length=9,choices=AccessType.choices)

    def getAccess(self):
        return self.access
