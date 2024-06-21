from django.db import models

# Create your models here.
class AccessType(models.TextChoices):
    ADMIN = "admin"
    ALUNO = "aluno"
    PROFESSOR = "professor"

class Login(models.Model):
    id=models.IntegerField(primary_key=True)
    login=models.EmailField()
    password=models.CharField(max_length=50)
    access=models.CharField(max_length=9,choices=AccessType.choices)

    def getAccess(self):
        return self.access

class Endereco(models.Model):
    id=models.IntegerField(unique=True,primary_key=True)
    logradouro=models.CharField(max_length=100)
    numero=models.IntegerField()
    bairro=models.CharField(max_length=100)
    uf=models.CharField(max_length=2)

class Professor(models.Model):
    matricula=models.IntegerField(max_length=10,primary_key=True,default="0000000000")
    cpf=models.BigIntegerField(max_length=11, default="00000000000")
    nome=models.CharField(max_length=50)
    endereco=models.ForeignKey(Endereco,on_delete=models.CASCADE,default=(0000,"n/a",00,"n/a","00"))
    telefone=models.CharField(max_length=11,default=00000000000)
    cursosMinistrados=[models.CharField]
    nivelEscolaridade=models.CharField
    formacao=[models.CharField]
    dataContratacao=models.DateField
    disciplinasMinistradas=[models.CharField]
    login=models.ForeignKey(Login,on_delete=models.CASCADE,default=00)    

class Disciplina(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    professores=models.ManyToManyField(Professor)
    conteudo=[models.FileField]
    cargaHoraria=models.IntegerField()
    horario=models.DateField()

class Aluno(models.Model):
    matricula=models.IntegerField(max_length=10,primary_key=True,default="0000000000")
    cpf=models.BigIntegerField(max_length=11, default="00000000000")
    nome=models.CharField(max_length=200)
    endereco=models.OneToOneField(Endereco,on_delete=models.CASCADE,default=("n/a",00,"n/a","00"))
    telefone=models.CharField(max_length=11,default=00000000000)
    dataAdmissao=models.DateField(auto_now_add=True)
    turmaCod=models.CharField(max_length=8)
    disciplinas=models.ManyToManyField(Disciplina)
    login=models.ForeignKey(Login,on_delete=models.CASCADE,default=00)

class Turma(models.Model):
    codigo=models.CharField(max_length=8)
    periodo=models.IntegerField(max_length=2)
    sala=models.CharField(max_length=20)
    dataAbertura=models.DateField()
    quantidadeAlunos=models.IntegerField(max_length=4)
