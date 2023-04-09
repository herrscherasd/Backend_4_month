from django.shortcuts import render
from blog.models import Post

def get_index(request):
    context = {
        "title" : "Главная страница",
        "my_list" : [1, 2, 3, 4]
    }
    return render(request, "blog/index.html", context=context)
    

def get_about(request):
    context = {
        "title" : "Страница о нас"
    }
    return render(request, "blog/about.html", context=context)

def get_contacts(request):
    context = {
        "title" : "Как с нами связаться"
    }
    return render(request, "blog/contacts.html", context=context)

def get_post(request, pk):
    post = Post.objects.get(id=pk)
    context =  {
        "post" : post,
    }
    return render(request, "blog/post_detail.html", context)

def post_create(request):
    return render(request, 'blog/post_create.html', context=None)

def post_update(request):
    return render(request, 'blog/post_update.html', context=None)