from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post

class IndexView(generic.ListView):
    # model = Post 
    template_name = "blog/index.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]

#CREATE
class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "blog/post_detail.html"

#DELETE
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('index-page')

class PostDeleteConfirimView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete_confirm.html"


#UPDATE
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy("post-update")
    fields = ["title", "content"]

class AboutView(generic.TemplateView):
    template_name = "blog/about.html"

class ContactsView(generic.TemplateView):
    template_name = "blog/contacts.html"
