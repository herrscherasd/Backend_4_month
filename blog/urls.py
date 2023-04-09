from django.urls import path
from blog import views

urlpatterns = [ 
    path("", views.get_index, name = "index-page"),
    path("about/", views.get_about, name = 'about-view'),
    path("contacts/", views.get_contacts, name = 'contacts-view'),
    path("post/<int:pk>", views.get_post, name = 'post_detail'),
    path("postupdate/", views.post_update, name = 'post_update-view'),
    path("postcreate/", views.post_create, name = 'post_create-view'),
]