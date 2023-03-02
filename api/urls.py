from django.urls import include, path
from rest_framework_nested import routers

from . import views

# 
app_name = 'api'

router = routers.DefaultRouter()
router.register(r'ops', views.OpsViewSet, basename="ops" )
#router.register(r'solicitacoes', views.SolicitacaoViewSet, basename="solicitacoes" )
#router.register(r'integrantes', views.IntegrantesViewSet, basename="integrantes" )

nested_router = routers.NestedDefaultRouter(router, r'ops', lookup="operacao")
nested_router.register(r"solicitacoes", views.SolicitacaoViewSet, basename="solicitacoes-ops")
nested_router.register(r"integrantes", views.IntegrantesViewSet, basename="integrantes-ops")

nested2_router = routers.NestedDefaultRouter(nested_router, r'solicitacoes', lookup="solicitacao")
nested2_router.register(r"celulares", views.CelularViewSet, basename="cel")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('', include(nested2_router.urls)),
]
