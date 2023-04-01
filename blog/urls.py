from django.urls import path
from blog import views

urlpatterns = [ 
    path("hello/", views.hello, name = "hello-view"),
]