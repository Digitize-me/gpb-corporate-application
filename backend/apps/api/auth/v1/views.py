from rest_framework_simplejwt.views import (
    TokenObtainPairView as BaseTokenObtainPairView,
    TokenRefreshView as BaseTokenRefreshView,
)

from .serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)


class TokenObtainPairView(BaseTokenObtainPairView):
    """Представление для получения токена доступа"""

    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(BaseTokenRefreshView):
    """Представление для обновления токена доступа"""

    serializer_class = TokenRefreshSerializer
