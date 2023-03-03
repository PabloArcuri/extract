from urllib import request
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
<<<<<<< HEAD
from rest_framework.decorators import action
=======
>>>>>>> 74d39165b92f301d30209a724ad68f7c85ecb5a1
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
<<<<<<< HEAD

    # def perform_update(self, serializer):
    #     integrantes = serializer.validated_data.get('integrantes')
    #     integrantes.append(self.request.user)
    #     serializer.save(integrantes=integrantes)
   
=======
    def get_queryset(self):
        return Operacao.objects.filter(integrantes = self.request.user)      
>>>>>>> 74d39165b92f301d30209a724ad68f7c85ecb5a1
   
        
class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Solicitacao.objects.filter(operacao__id = self.kwargs["operacao_pk"], operacao__integrantes = self.request.user)
    
    def perform_create(self, serializer):
        operacao = self.kwargs["operacao_pk"]
        serializer.save(operacao_id = operacao)
        


class IntegrantesViewSet(viewsets.ModelViewSet):
    serializer_class = IntegrantesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.filter( operacao_integrantes=self.kwargs["operacao_pk"])
    

class CelularViewSet(viewsets.ModelViewSet):
    serializer_class = CelularSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Celular.objects.filter(solicitacao = self.kwargs["solicitacao_pk"], solicitacao__operacao__integrantes = self.request.user)
        return queryset



