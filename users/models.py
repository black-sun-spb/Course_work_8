from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Пользователь
class User(AbstractUser):
    """Расширенная модель пользователя, пока пустая"""
    pass


# Профиль пользователя
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    telegram_chat_id = models.CharField(
        max_length=64,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
