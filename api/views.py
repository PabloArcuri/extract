from urllib import request
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Operacao, Solicitacao, Celular, Nuvem, Resposta

from .serializer import *


class OpsViewSet(viewsets.ModelViewSet):
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        integrantes = [self.request.user]
        serializer.save(criador = self.request.user, integrantes=integrantes)

    # def perform_update(self, serializer):
    #     integrantes = serializer.validated_data.get('integrantes')
    #     integrantes.append(self.request.user)
    #     serializer.save(integrantes=integrantes)
    
    
   
        
class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer

    def get_queryset(self):
        return Solicitacao.objects.filter(solicitacao__operacao__id = self.kwargs["operacao_pk"])
        


class IntegrantesViewSet(viewsets.ModelViewSet):
    serializer_class = IntegrantesSerializer
    
    def get_queryset(self):
        return User.objects.filter(Operacao__integrantes=self.kwargs["operacao_pk"])




