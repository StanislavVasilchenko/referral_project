from django.db import models

from config import settings
from users.models import NULLABLE


class ReferralCode(models.Model):
    name = models.CharField(max_length=255, verbose_name="code_name")
    description = models.TextField(verbose_name="description")
    date_created = models.DateField(auto_now_add=True, verbose_name="date created")
    lifetime = models.PositiveSmallIntegerField(default=1, verbose_name="lifetime")  # время жизни кода
    user_owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owner")

    user_subscriber = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.SET_DEFAULT,
                                        default=None,
                                        related_name="subscriber",
                                        **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="active")

    def __str__(self):
        return f'{self.name} - {self.date_created} - {self.lifetime} - {self.is_active}'

    class Meta:
        verbose_name = "referral code"
        verbose_name_plural = "referral"
        ordering = ["-date_created"]
