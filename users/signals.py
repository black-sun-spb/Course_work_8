from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, User


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    """
    Создает профиль при создании пользователя, если его ещё нет.
    """
    Profile.objects.get_or_create(user=instance)
