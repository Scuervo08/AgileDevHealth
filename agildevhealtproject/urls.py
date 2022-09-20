from django.urls import include,path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from agildevhealtapp import views
urlpatterns = [
                path('login/', TokenObtainPairView.as_view()),
                path('refresh/', TokenRefreshView.as_view()),
                path('user/', views.UserCreateView.as_view()),
                path('user/<int:pk>/', views.UserDetailView.as_view()),
            ]