from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('shorten/', views.ShortenUrl.as_view()),
    path('register/', views.RegisterNewUser.as_view()),
    path('login/', views.Login.as_view()),
    path('user/urls/', views.GetUserUrls.as_view()),
    path('destination/', views.GetDestinationUrl.as_view()),
    #path('get-login-token', obtain_auth_token, name='api_token_auth'),


]
