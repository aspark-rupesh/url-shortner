from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import  logout
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from user.forms import CustomUserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect(reverse_lazy("login"))

class UserRegisterView(CreateView):
    model = User
    queryset = User.objects.all()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'create.html'

