from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email address')
    is_referrer = models.BooleanField(default=False, verbose_name='referrer', **NULLABLE)
    is_referral = models.BooleanField(default=False, verbose_name='referral', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} - (referrer: {self.is_referrer}, referral: {self.is_referral})'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
