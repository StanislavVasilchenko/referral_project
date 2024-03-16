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
    subscriber = models.ForeignKey('self', **NULLABLE, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} - (referrer: {self.is_referrer}, referral: {self.subscriber})'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
