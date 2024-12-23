from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterView, login_view, OrderViewSet, ProductViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', login_view),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
] + router.urls