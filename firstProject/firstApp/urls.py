from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path("hello/", hello),
    path("echo/", echo),
    path("auth/token/", TokenObtainPairView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
]