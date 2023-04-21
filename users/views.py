from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from users.forms import UserRegistrationForm

# Create your views here.

# def register(request):
#     if request.method == "POST":
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.clean_password2())
#             new_user.save()
#             return render(request, "registration/register_done.html", {'user' : new_user})
    
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'registration/register.html', {"form" : user_form})


class RegisterView(generic.FormView):
    form_class=UserRegistrationForm
    success_url=reverse_lazy('register-done')
    template_name='registration/register.html'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password2'])
        new_user.save()
        return super().form_vaild(form)
    
