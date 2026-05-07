from django.db import models
 
class Cliente(models.Model):
    nome=models.CharField(verbose_name="Nome", max_length=100)
    cpf= models.CharField(verbose_name="cpf",max_length=14)
    telefone=models.CharField(verbose_name="telefone",max_length=14)
    datadenascimento=models.DateField(verbose_name="data de nascimento")
 
    def __str__(self):
        return self.nome
 

