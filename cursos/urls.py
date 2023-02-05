from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (CursoAPIView,
    CursosAPIView,
    AvaliacoesAPIView,
    AvaliacaoAPIView,
    CursoViewSet,
    AvaliacaoViewSet,)


# Versão 2 da api
router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)



# Versão 1 da api
urlpatterns = [

    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:id>', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_id>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_id>/avaliacoes/<int:avaliacao_id>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_id>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    
]

