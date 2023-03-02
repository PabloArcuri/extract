from urllib import request
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Operacao, Solicitacao, Celular, Nuvem, Resposta

from .serializer import *


class OpsViewSet(viewsets.ModelViewSet):
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        integrantes = [self.request.user]
        serializer.save(criador = self.request.user, integrantes=integrantes)

      
   
        
class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer

    def get_queryset(self):
        return Solicitacao.objects.filter(operacao__id = self.kwargs["operacao_pk"])
    
    def perform_create(self, serializer):
        operacao = self.kwargs["operacao_pk"]
        serializer.save(operacao_id = operacao)
        


class IntegrantesViewSet(viewsets.ModelViewSet):
    serializer_class = IntegrantesSerializer
    
    def get_queryset(self):
        return User.objects.filter( operacao_integrantes=self.kwargs["operacao_pk"])
    
class CelularViewSet(viewsets.ModelViewSet):
    serializer_class = CelularSerializer
    
    def get_queryset(self):
        queryset = Celular.objects.filter(solicita)




