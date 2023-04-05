from django.urls import path
from blog import views

urlpatterns = [ 
    path("", views.get_index, name = "index-page"),
    path("about/", views.get_about, name = 'about-view'),
    path("contacts/", views.get_contacts, name = 'contacts-view'),
]