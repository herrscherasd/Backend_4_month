from django.urls import path
from blog import views

urlpatterns = [ 
    path("", views.IndexView.as_view(), name = "index-page"),
    path("about/", views.AboutView.as_view(), name = 'about-view'),
    path("contacts/", views.ContactsView.as_view(), name = 'contacts-view'),
    path("post/<int:pk>", views.PostDetailView.as_view(), name = 'post-detail'),
    path("post/update/<int:pk>", views.PostUpdateView.as_view(), name = 'post-update'),
    path("post/create/", views.PostCreateView.as_view(), name = 'post-create'),
    path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name = "post-delete"),
]