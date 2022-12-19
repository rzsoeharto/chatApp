from django.urls import path
from . import views
from .views import CheckAuthenticatedView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView

urlpatterns = [
    path("authenticated/", CheckAuthenticatedView.as_view()),
    path("create-listing/", views.createListing),
    path("login/", MyTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("register/", views.registerView),
]
