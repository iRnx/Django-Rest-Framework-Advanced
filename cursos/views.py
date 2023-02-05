from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

"""
API versão 1
"""

# List e create = get e post
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# Update e Destroy = atualizar e deletar
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    lookup_field = 'id'


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


    def get_queryset(self):
        if self.kwargs.get('curso_id'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_id'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    lookup_field = 'id'


    def get_object(self):
        if self.kwargs.get('curso_id'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_id'),
                                    id=self.kwargs.get('avaliacao_id'))

        return get_object_or_404(self.get_queryset(), id=self.kwargs.get('avaliacao_id'))


"""
API versão 2
"""


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get']) # este decorator com detail true para criar a rota
    def avaliacoes(self, request, pk=None):

        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # curso = self.get_object()
        # print(curso)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)



class AvaliacaoViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer




# class AvaliacaoViewSet(viewsets.ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer

