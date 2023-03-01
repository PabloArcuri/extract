from django.contrib import admin
from .models import Operacao, Solicitacao, Celular, Nuvem, Resposta
# Register your models here.

admin.site.register(Operacao)
admin.site.register(Solicitacao)
admin.site.register(Celular)
admin.site.register(Nuvem)
admin.site.register(Resposta)

