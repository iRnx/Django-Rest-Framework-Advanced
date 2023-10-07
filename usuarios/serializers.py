from rest_framework import serializers

from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    is_staff = serializers.BooleanField(
        label="Membro da Equipe",
        help_text="Indica que usuário consegue acessar o site de administração."
    )

    is_superuser = serializers.BooleanField(
        label="SuperUsuário",
        help_text="Indica que este usuário tem todas as permissões sem atribuí-las explicitamente."
    )

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'username', 'password', 'password_confirm', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):

        password = validated_data['password']
        password_confirm = validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})

        if  'password_confirm' in validated_data:
            validated_data.pop('password_confirm')

        user = Usuario.objects.create(**validated_data)

        return user

    