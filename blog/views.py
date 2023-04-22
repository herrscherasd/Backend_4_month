from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics


from blog.forms import CommentForm, PostForm
from blog.models import Post, Comment
from blog.serializers import PostSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = "pk"

class PostCreateAPIView(generics.CreateAPIView):
    serializer_class =PostSerializer
    queryset = Post.objects.all()
    

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer


class IndexView(generic.ListView):
    # model = Post 
    template_name = "blog/index.html"
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ''
        return context

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy("index-page")
    form_class = PostForm




#CREATE
class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "blog/post_detail.html"
    extra_context = {"form" : CommentForm()}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = CommentForm()
    #     return context

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form  = CommentForm(request.POST)
        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()
        # username = request.POST.get("username_input", None)
        # text = request.POST.get("text", None)
        # if username and text != "":
        #     print("У нас все есть")
        #     comment = Comment.objects.create(username=username, text=text, post=post)
        #     comment.save()
        return redirect("post-detail", pk)

#DELETE

class PostDeleteConfirimView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete_confirm.html"
    success_url = reverse_lazy("index-page")


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
