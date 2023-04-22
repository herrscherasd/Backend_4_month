from django.urls import path
from users.views import RegisterView, RegisterDone

urlpatterns = [
    path("users/register/", RegisterView.as_view(), name="register"),
    path("users/register/registerdone", RegisterDone.as_view(), name='register-done')
]