from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from apps.core.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    username = models.CharField(
        max_length=100,
        unique=True
    )
    kakao_user_id = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['kakao_user_id']

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = verbose_name
