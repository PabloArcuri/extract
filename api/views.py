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

    @action(detail=True, methods = ['get'])
    def solicitacoes(self, request, pk=None, *args, **kwargs):
        queryset = Solicitacao.objects.filter(pk=pk)
        self.serializer_class = OperacaoSerializer
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data) 
    
    
   
        
class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
    




