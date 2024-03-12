from django.urls import path

from users.apps import UsersConfig
from users.views import UserRegistrationsAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', UserRegistrationsAPIView.as_view(), name='index')
]