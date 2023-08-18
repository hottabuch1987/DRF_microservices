from django.urls import path
from .views import SignupAPIView, me
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', SignupAPIView.as_view(), name='create'),
    path('me/', me, name='me'),


]