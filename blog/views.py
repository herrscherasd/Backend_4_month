from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    heading = """<h1> Закголовок 1 lvl</h1>
    <h2> Загаловок 2 lvl
    """

    return HttpResponse("Hello", headers={"name": "Alex"}, status = 500)
    

def get_about(request):
    return HttpResponse("Какая-нибудь строка")

def get_contacts(request):
    return HttpResponse("Какая-нибудь строка 2")
