from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post

class IndexView(generic.ListView):
    # model = Post 
    template_name = "blog/index.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'
    extra_context = {"title" : "Главная страница"}

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
    success_url = reverse_lazy('index-page')

#UPDATE
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy("post-update")
    fields = ["title", "content"]

# # def get_index(request):
#     posts = Post.objects.all
# #     context = {
# #         "title" : "Главная страница",
# #         "my_list" : [1, 2, 3, 4],
#             'posts' : posts
# #     }
# #     return render(request, "blog/index.html", context=context)
    

def get_about(request):

    return render(request, "blog/about.html", context= None)

def get_contacts(request):

    return render(request, "blog/contacts.html", context=None)

# def get_post(request, pk):
#     post = Post.objects.get(id=pk)
#     context =  {
#         "post" : post,
#     }
#     return render(request, "blog/post_detail.html", context)

def post_create(request):
    return render(request, 'blog/post_create.html', context=None)

def post_update(request):
    return render(request, 'blog/post_update.html', context=None)