from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = ('id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'ativo')

    curso = serializers.StringRelatedField()


class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship

    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field

    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    # view_name='avaliacao-detail' pq os viewsets cria a rota automaticamente e avaliacao por conta do model e detail pq o viewset cria

    # Primary Key Related Field
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # String Related Field
    avaliacoes = serializers.StringRelatedField(many=True, read_only=True)
    

    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'url', 'criacao', 'ativo', 'avaliacoes')
