from django.shortcuts import render
from users.forms import UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.clean_password2())
            new_user.save()
            return render(request, "registration/register_done.html", {'user' : new_user})
    
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {"form" : user_form})