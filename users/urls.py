from django.urls import path
from users.views import register

urlpatterns = [
    path("users/register/", register, name="register")
]