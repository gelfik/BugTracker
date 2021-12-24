from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (LoginAPIView, RegistrationAPIView, UserDataAPIView)

app_name = 'UserProfileApp'

LoginAPIView.http_method_names = ('post', 'options',)
RegistrationAPIView.http_method_names = ('post', 'options',)
UserDataAPIView.http_method_names = ('get', 'options',)

urlpatterns = [
    path('/login', LoginAPIView.as_view()),
    path('/register', RegistrationAPIView.as_view()),
    path('/user', UserDataAPIView.as_view()),
]
