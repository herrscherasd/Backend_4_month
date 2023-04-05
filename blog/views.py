from django.shortcuts import render

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
    return render(request, "blog/about.html", context=None)

def get_contacts(request):
    context = {
        "title" : "Как с нами связаться"
    }
    return render(request, "blog/contacts.html", context=None)