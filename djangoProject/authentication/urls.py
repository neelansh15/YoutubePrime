from django.urls import path
from .views import MyObtainTokenPairView,RegisterView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView



urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]