from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserRegistrationsAPIView, UserDetailAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('registration/', UserRegistrationsAPIView.as_view(), name='registration_user'),
    path('referral/<int:pk>/', UserDetailAPIView.as_view(), name='sub_list'),
]