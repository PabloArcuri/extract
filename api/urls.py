from django.urls import include, path
from rest_framework import routers

from . import views

# 
app_name = 'api'

router = routers.DefaultRouter()
router.register(r'ops', views.OpsViewSet, basename="ops" )
router.register(r'solicitacoes', views.SolicitacaoViewSet, basename="solicitacoes" )

urlpatterns = [
    path('', include(router.urls)),
]
