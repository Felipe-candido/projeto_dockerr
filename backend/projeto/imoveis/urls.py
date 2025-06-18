from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r"registrar", views.cadastro_imovel, basename='registro')
router.register(r"list", views.imovel_list_cidade, basename='imovel-list')
router.register(r'chacaras', views.ChacaraViewSet)
router.register(r'cidade', views.imovel_list_cidade, basename='imovel-cidade')
router.register(r'destaque', views.imoveis_destaque, basename='imoveis-destaque')
router.register(r'comodidades', views.ComodidadeViewSet, basename='comodidades')
router.register(r'destaque-v2', views.ImoveisDestaqueView, basename='imoveis-destaque-v2')





urlpatterns = [
    path('', include(router.urls)),
    path('propriedade/', views.imovel_por_id.as_view()),
    path('editar/<int:id>/', views.EditarImovelView.as_view()),
    path('usuario/', views.ImoveisUsuarioView.as_view()),
    path('destaque/', views.ImoveisDestaqueView.as_view({'get': 'list'}), name='imoveis-destaque'),
    path('avaliacao/', views.AvaliacaoImovelView.as_view(), name='imovel-avaliacao'),
]
