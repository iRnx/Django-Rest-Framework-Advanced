from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Avaliacao


@receiver(pre_delete, sender=Avaliacao)
def teste(sender, instance, using, **kwargs):
    print(f'Passei por aqui antes de deletar o "{instance.nome} e {instance.email}"')
    for valor in Avaliacao.objects.all():
        print(valor)
    