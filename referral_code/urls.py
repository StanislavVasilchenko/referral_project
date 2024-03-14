from django.urls import path

from referral_code.apps import ReferralCodeConfig
from referral_code.views import ReferralCodeCreateAPIView

app_name = ReferralCodeConfig.name

urlpatterns = [
    path('create/', ReferralCodeCreateAPIView.as_view(), name='referral-code-create')
]
