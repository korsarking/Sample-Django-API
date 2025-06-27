from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

from src.accounts.views import UserViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r"accounts", UserViewSet, basename="accounts")

urlpatterns = [
    path(r"accounts/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(r"accounts/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
