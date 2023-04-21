from django.urls import path
from users.views import RegisterView

urlpatterns = [
    path("users/register/", RegisterView.as_view(), name="register")
]