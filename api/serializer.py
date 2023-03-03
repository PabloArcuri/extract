from rest_framework import serializers
from .models import Operacao, Solicitacao, Celular, Nuvem, Resposta
from django.contrib.auth.models import User


class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = '__all__'

class IntegrantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CriadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class OperacaoSerializer(serializers.ModelSerializer):
    solicitacao = SolicitacaoSerializer(many=True, read_only=True)
    integrantes = IntegrantesSerializer(many=True, read_only=True)
    criador = CriadorSerializer(many=False, read_only=True)
    
    class Meta:
        model = Operacao
        
        fields = [
            'id',
            'nome',
            'data_criacao',
            'criador',
            'integrantes',
            'solicitacao'
        ]
        



class CelularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celular
        fields = '__all__'

class NuvemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nuvem
        fields = '__all__'

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'