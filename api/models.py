from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Operacao(models.Model):

    nome = models.CharField( max_length=150)
    data_criacao = models.DateField(auto_now_add=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operacao_criador')
    integrantes = models.ManyToManyField(User, related_name='operacao_integrantes')
    class Meta:
        verbose_name = ("Operacao")
        verbose_name_plural = ("Operacoes")

    def __str__(self):
        return self.nome
    

class Solicitacao(models.Model):

    tipo_choices = [
        ('Nuvem', 'Nuvem'),
        ('Celular', 'Celular'),
    ]
    
    tipo = models.CharField( choices=tipo_choices, max_length=50)
    operacao = models.ForeignKey(Operacao, on_delete=models.CASCADE, related_name='op_solicitacao')
    situacao = models.CharField(max_length=50)
    data_entrada = models.DateField(default=timezone.now)
    ipl = models.CharField(max_length=50, blank=True, null=True)
    referencia = models.CharField(max_length=120, blank=True, null=True)
    Solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes', blank=True, null = True)
    oficio_entrada = models.CharField(max_length=120, blank=True, null=True)
    autorizacao_judicial = models.CharField(max_length=200, blank=True, null=True)
    
    
    
    
    
    class Meta:
        verbose_name = ("Solicitacao")
        verbose_name_plural = ("Solicitacoes")

    def __str__(self):
        return str(self.id)  

class Celular(models.Model):

    auto_apreensao = models.CharField(max_length=50, blank=True, null=True)
    n_item = models.CharField(max_length=50, blank=True, null=True)
    tipo_dispositivo = models.CharField(max_length=50)
    marca_dispositivo = models.CharField(max_length=50)
    modelo_dispositivo = models.CharField(max_length=50)
    imei_dispositivo = models.CharField(max_length=50)
    obs_entrada = models.CharField(max_length=500, blank=True, null=True)
    lacre_entrada = models.CharField(max_length=50,blank=True, null=True)
    solicitacao = models.ForeignKey(Solicitacao, related_name="celular", on_delete=models.CASCADE)
    
    

    class Meta:
        verbose_name = ("Celular")
        verbose_name_plural = ("Celulares")

    def __str__(self):
        return str(self.id)+' celular'


class Nuvem(models.Model):

    empresa = models.CharField(max_length=50)    
    usuario = models.CharField(max_length=150)    
    bsid = models.CharField(max_length=150)    
    obs_entrada = models.CharField(max_length=150, null=True, blank=True)    

    class Meta:
        verbose_name = ("nuvem")
        verbose_name_plural = ("nuvens")

    def __str__(self):
        return str(self.id)+' nuvem'



class Resposta(models.Model):

    data_saida = models.DateTimeField(default=timezone.now)
    oficio_saida = models.CharField(max_length=50, null=True, blank=True)
    destinatario = models.CharField(max_length=50)
    obs_saida = models.CharField(max_length=500, null=True, blank=True)
    resultados = models.CharField(max_length=500, null=True, blank=True)
    lacre_saida = models.CharField(max_length=50, null=True, blank=True)
    n_ipj = models.CharField(max_length=50,null=True, blank=True)
    hash = models.CharField(max_length=50, null=True, blank=True)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.DO_NOTHING, related_name='resposta')

    class Meta:
        verbose_name = ("resposta")
        verbose_name_plural = ("respostas")

    def __str__(self):
        return str(self.id)

