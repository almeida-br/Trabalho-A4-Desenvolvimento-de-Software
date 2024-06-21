# Generated by Django 4.2.13 on 2024-06-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_aluno_cpf_alter_aluno_telefone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aluno",
            name="turmaCod",
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name="endereco",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name="turma",
            name="codigo",
            field=models.CharField(max_length=8),
        ),
    ]
